import threading
import mido
import numpy as np
import pygame

# Initialize Pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=1024)

def midi_to_freq(note):
    return 440.0 * (2.0 ** ((note - 57) / 12.0))

def generate_sine_wave(freq, duration=1.0, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(freq * t * 2 * np.pi)
    tone = np.int16(tone * 32767)
    return tone

def play_tone(freq, duration=1.0):
    tone = generate_sine_wave(freq, duration)
    sound = pygame.sndarray.make_sound(tone)
    sound.play()
    pygame.time.wait(int(len(tone) / 44.1))

# Handle MIDI input in a separate thread



def handle_midi_input():
    midi_input = None
    for input_name in mido.get_input_names():
        print(f"Found MIDI input: {input_name}")
        if "LPK25 mk2" in input_name:  # Replace with your MIDI Keyboard name
            midi_input = mido.open_input(input_name)
            break

    if not midi_input:
        raise Exception("MIDI Keyboard not found.")

    try:
        while True:
            for msg in midi_input.iter_pending():
                if msg.type == 'note_on' and msg.velocity > 0:
                    freq = midi_to_freq(msg.note)
                    threading.Thread(target=play_tone, args=(freq,)).start()
                elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                    # Handle note off event if needed
                    pass
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        midi_input.close()

# Start MIDI handling in a separate thread
midi_thread = threading.Thread(target=handle_midi_input)
midi_thread.start()

# Keep the main thread alive
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Shutting down...")

pygame.mixer.quit()
