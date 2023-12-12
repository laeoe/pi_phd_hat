import pygame
import os
import time

import mido

# Find and open the MIDI Keyboard
midi_input = None
for input_name in mido.get_input_names():
    print(f"Found MIDI input: {input_name}")
    if "LPK25 mk2" in input_name:  # Replace with your MIDI Keyboard name
        midi_input = mido.open_input(input_name)
        break

if not midi_input:
    raise Exception("MIDI Keyboard not found.")

# Initialize Pygame mixer
pygame.mixer.init()

# Path where the samples are stored
samples_path = "/home/pi/pi_phd_hat/assets/key_samples"

key_samples = {}
# get all key samples in the folder
for file in os.listdir(samples_path):
    if file.endswith(".wav"):
        key_samples[file.split(".")[0]] = pygame.mixer.Sound(os.path.join(samples_path, file))


def play_key(note_number):
    note_number = str(note_number)
    """ Play the sample corresponding to the given note number """
    if note_number in key_samples:
        print(f"Playing note {note_number}")
        key_samples[note_number].play()


# try: 
#     print("testing audio playback")
#     play_key(60)
#     time.sleep(1)
# except KeyboardInterrupt:
#     print("Exiting...")

try:
    print("Reading MIDI input. Press Ctrl+C to stop.")
    for msg in midi_input:
        if msg.type == 'note_on' and msg.velocity > 0:
            print(msg)
            play_key(msg.note)
        elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity > 0):
            # Handle note off event if needed
            pass
except KeyboardInterrupt:
    print("Exiting...")

pygame.mixer.quit()
