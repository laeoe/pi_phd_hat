import numpy as np
import pyaudio

def generate_sine_wave(freq, duration=1.0, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(freq * t * 2 * np.pi)
    return tone.astype(np.float32)

def play_tone(stream, frequency=440.0, duration=1.0, sample_rate=44100):
    samples = generate_sine_wave(frequency, duration, sample_rate)
    stream.write(samples.tobytes())

if __name__ == "__main__":
    p = pyaudio.PyAudio()
    
    # Open a stream with appropriate settings
    stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=True,
                frames_per_buffer=4096)

    print("Playing tone...")
    play_tone(stream)
    print("Done")

    stream.stop_stream()
    stream.close()
    p.terminate()
