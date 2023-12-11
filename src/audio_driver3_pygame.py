import pygame
import numpy as np

# Initialize Pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=4096)


def generate_sine_wave(freq, duration=1.0, sample_rate=44100):
    # Generate time values
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    # Generate sine wave data
    tone = np.sin(freq * t * 2 * np.pi)
    # Normalize to 16-bit range
    tone = np.int16(tone * 32767)
    return tone

def play_tone(tone):
    # Convert numpy array to sound buffer
    sound = pygame.sndarray.make_sound(tone)
    # Play sound
    sound.play()
    # Wait for the sound to finish playing
    pygame.time.wait(int(len(tone) / 44.1))

if __name__ == "__main__":
    frequency = 440  # Frequency in Hz (A4 note)
    duration = 5    # Duration in seconds
    tone = generate_sine_wave(frequency, duration)
    play_tone(tone)
    pygame.mixer.quit()
