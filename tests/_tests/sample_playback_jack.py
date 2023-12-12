import jack
import numpy as np
import threading
from concurrent.futures import ThreadPoolExecutor
import mido
import wave

class JackAudioPlayer:
    def __init__(self, samples_path):
        self.samples_path = samples_path
        self.client = jack.Client("PianoPlayer")
        self.output_port = self.client.outports.register("output")
        self.audio_data = {}
        self.thread_pool = ThreadPoolExecutor(max_workers=10)

    def preload_audio_data(self):
        for note in range(97):
            file_name = f"{self.samples_path}/{note}.wav"
            with wave.open(file_name, 'rb') as wf:
                frames = wf.readframes(wf.getnframes())
                self.audio_data[note] = np.frombuffer(frames, dtype=np.int16)

    def play(self, note_number):
        if note_number in self.audio_data:
            self.thread_pool.submit(self._play_note, note_number)

    def _play_note(self, note_number):
        # Convert int16 data to float32 and send to JACK output
        data = (self.audio_data[note_number].astype(np.float32) - 32768) / 32768
        self.output_port.write(data)

    def close(self):
        self.thread_pool.shutdown(wait=True)
        self.client.deactivate()
        self.client.close()

# Rest of the script remains largely the same


samples_path = "/home/pi/pi_phd_hat/assets/key_samples"

audio_player = JackAudioPlayer(samples_path)

audio_player.play(57)


# client = jack.Client("MyClient")

# # Create ports
# outport = client.outports.register("output")

# # Activate the client
# client.activate()

# # Now you can use the client and ports to process audio
# # ...

# # When done, deactivate and close the client
# client.deactivate()
# client.close()