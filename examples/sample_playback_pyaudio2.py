# # So far the best running version

import pyaudio
import wave
import threading
from concurrent.futures import ThreadPoolExecutor
import mido

class AudioPlayer:
    def __init__(self, samples_path):
        self.samples_path = samples_path
        self.pyaudio_instance = pyaudio.PyAudio()
        self.audio_data = {}  # Dictionary to store preloaded audio data
        self.thread_pool = ThreadPoolExecutor(max_workers=10)  # Limit the number of threads

    def preload_audio_data(self):
        """ Preload audio data for each note """
        for note in range(121):  # Assuming 121 keys
            file_name = f"{self.samples_path}/{note}.wav"
            with wave.open(file_name, 'rb') as wf:
                self.audio_data[note] = wf.readframes(wf.getnframes())

    def play(self, note_number):
        if note_number in self.audio_data:
            print(f"Playing note {note_number}")
            self.thread_pool.submit(self._play_note, note_number)

    def _play_note(self, note_number):
        stream = self.pyaudio_instance.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True)
        stream.write(self.audio_data[note_number])
        stream.stop_stream()
        stream.close()

    def close(self):
        self.thread_pool.shutdown(wait=True)
        self.pyaudio_instance.terminate()

# Initialize and preload audio data
samples_path = "/home/pi/pi_phd_hat/assets/key_samples"

audio_player = AudioPlayer(samples_path)
audio_player.preload_audio_data()

# audio_player.play(57)

# MIDI handling (similar to your existing code)
# Find and open the MIDI Keyboard
midi_input = None
for input_name in mido.get_input_names():
    print(f"Found MIDI input: {input_name}")
    if "LPK25 mk2" in input_name:  # Replace with your MIDI Keyboard name
        midi_input = mido.open_input(input_name)
        break

if not midi_input:
    raise Exception("MIDI Keyboard not found.")

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
