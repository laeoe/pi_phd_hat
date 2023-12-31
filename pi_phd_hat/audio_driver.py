# so far best working audio driver for playing back pregenerated key samples

import pyaudio
import wave
from concurrent.futures import ThreadPoolExecutor
import os


import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

# Your code here


class AudioPlayer:
    def __init__(self):
        # Determine the base path relative to the current file
        self.base_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'key_samples')
        self.pyaudio_instance = pyaudio.PyAudio()
        self.audio_data = {}  # Dictionary to store preloaded audio data
        self.thread_pool = ThreadPoolExecutor(max_workers=3)  # Limit the number of threads
        self.preload_audio_data()

    def preload_audio_data(self):
        """ Preload audio data for each note """
        for note in range(121):  # Assuming 121 keys
            file_path = os.path.join(self.base_path, f'{note}.wav')
            with wave.open(file_path, 'rb') as wf:
                self.audio_data[note] = wf.readframes(wf.getnframes())
        # preload the files for the other audio
        # self.audio_data["hat_won"] = self._preload_other("hat_won.wav")

    def play(self, note_number):
        if note_number in self.audio_data:
            # print(f"Playing note {note_number}")
            self.thread_pool.submit(self._play_note, note_number)

    def _play_note(self, note_number):
        stream = self.pyaudio_instance.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True)
        stream.write(self.audio_data[note_number])
        stream.stop_stream()
        stream.close()

    def play_other(self, file_path, sample_rate):
        self.thread_pool.submit(self._play_other, file_path, sample_rate)
    
    def _play_other(self, file_path, sample_rate):
        stream = self.pyaudio_instance.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, output=True)
        with wave.open(file_path, 'rb') as wf:
            stream.write(wf.readframes(wf.getnframes()))
        stream.stop_stream()
        stream.close()
        

    def close(self):
        self.thread_pool.shutdown(wait=True)
        self.pyaudio_instance.terminate()
        # print("AudioPlayer closed")


if __name__ == "__main__":
    print("Testing audio driver")
    player = AudioPlayer()
    player.play(60)
    player._play_other("/home/pi/pi_phd_hat/assets/sounds/level_won.wav")
    player.close()
    print("Test finished")