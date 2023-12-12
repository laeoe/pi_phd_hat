# working abit better than pygame but still choppy

import pyaudio
import wave
import threading
import mido 

class AudioPlayer:
    def __init__(self, samples_path):
        self.samples_path = samples_path
        self.pyaudio_instance = pyaudio.PyAudio()

    def play(self, note_number):
        threading.Thread(target=self._play_note, args=(note_number,)).start()

    def _play_note(self, note_number):
        file_name = f"{self.samples_path}/{note_number}.wav"
        with wave.open(file_name, 'rb') as wf:
            stream = self.pyaudio_instance.open(
                format=self.pyaudio_instance.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
            data = wf.readframes(1024)
            while data:
                stream.write(data)
                data = wf.readframes(1024)
            stream.stop_stream()
            stream.close()

    def close(self):
        self.pyaudio_instance.terminate()

# Path where the samples are stored
samples_path = "/home/pi/pi_phd_hat/assets/key_samples"

# Find and open the MIDI Keyboard
midi_input = None
for input_name in mido.get_input_names():
    print(f"Found MIDI input: {input_name}")
    if "LPK25 mk2" in input_name:  # Replace with your MIDI Keyboard name
        midi_input = mido.open_input(input_name)
        break

if not midi_input:
    raise Exception("MIDI Keyboard not found.")

# Initialize AudioPlayer
audio_player = AudioPlayer(samples_path)


try:
    print("Reading MIDI input. Press Ctrl+C to stop.")
    for msg in midi_input:
        if msg.type == 'note_on' and msg.velocity > 0:
            print(msg)
            audio_player.play(msg.note)
        elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity > 0):
            # Handle note off event if needed
            pass
except KeyboardInterrupt:
    print("Exiting...")
# Cleanup
audio_player.close()

