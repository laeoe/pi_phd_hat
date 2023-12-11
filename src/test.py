import mido
from pyo import *
import numpy as np

# Initialize Pyo server
s = Server().boot()
s.start()


# Create a sine wave oscillator but don't play it yet
osc = Sine(freq=440, mul=0.1).out()
osc.stop()


# calculate the frequency of a piano key
def key_freq(key):
    a = 440 # Base tone at 440Hz
    return a * 2 **((key - 57) / 12) # currentely the number of a4 is wrong!


# Find and open the MIDI Keyboard
midi_input = None
for input_name in mido.get_input_names():
    print(f"Found MIDI input: {input_name}")
    if "LPK25 mk2" in input_name:  # Replace with your MIDI Keyboard name
        midi_input = mido.open_input(input_name)
        break

if not midi_input:
    raise Exception("MIDI Keyboard not found.")

# Function to process MIDI messages
def process_midi_message(msg):
    if msg.type == 'note_on' and msg.velocity > 0:
        # Start the oscillator with the frequency of the note
        # osc.freq = midi_to_freq(msg.note)
        osc.freq = key_freq(msg.note)
        osc.out()
        print(f"freq = {key_freq(msg.note)}")
    elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
        # Stop the oscillator
        osc.stop()

# Main loop to read MIDI messages
try:
    print("Reading MIDI input. Press Ctrl+C to stop.")
    for msg in midi_input:
        process_midi_message(msg)
        print(msg)
except KeyboardInterrupt:
    print("Exiting...")

# Clean up
s.stop()
