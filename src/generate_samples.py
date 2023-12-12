import numpy as np
from scipy.io.wavfile import write
import os
from pi_phd_hat.src._tests.piano_math import key_2freq


def generate_sine_wave(freq, duration, dampening, sample_rate):
    """ Generate sine wave corresponding to a given frequency """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(freq * t * 2 * np.pi)
    # Generate a an exponential dampening 
    tone *= np.exp(-t * dampening)
    # Normalize to 16-bit range
    tone = np.int16(tone * 32767)
    return tone

def save_tone(note_number, file_name, duration=0.5, dampening = 10, sample_rate=44100):
    """ Generate and save a tone as a WAV file """
    freq = key_2freq(note_number)
    tone = generate_sine_wave(freq, duration, dampening, sample_rate)
    write(file_name, sample_rate, tone)

# Directory to save the files
save_path = "/home/pi/pi_phd_hat/assets/key_samples"

# Ensure the directory exists
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Generate and save tones for the first 97 piano keys
for note in range(97):
    file_name = os.path.join(save_path, f"{note}.wav")
    save_tone(note, file_name)
    print(f"Saved {file_name}")
