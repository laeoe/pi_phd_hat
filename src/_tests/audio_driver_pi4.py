import sounddevice as sd 
import numpy as np 


def generate_sine_wave(freq, duration=1.0, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(freq * t * 2 * np.pi)
    return tone


if __name__ == "__main__": 
    print("Testing audio")
    tone = generate_sine_wave(440)
    sd.play(tone, 44100)
    sd.wait()
    print("Done")
