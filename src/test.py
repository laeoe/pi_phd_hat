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
def key_2freq(key):
    a = 440 # Base tone a4 = 440Hz
    return a * 2 **((key - 57) / 12)


# Find and open the MIDI Keyboard
midi_input = None
for input_name in mido.get_input_names():
    print(f"Found MIDI input: {input_name}")
    if "LPK25 mk2" in input_name:  # Replace with your MIDI Keyboard name
        midi_input = mido.open_input(input_name)
        break

if not midi_input:
    raise Exception("MIDI Keyboard not found.")
    

# Create the oscillators for the Keyboard
oscillators = {}
for note in range(128):  # MIDI has 128 notes
    oscillators[note] = Sine(freq=key_2freq(note))

# Function to process MIDI messages
def process_midi_message(msg):
    if msg.type == 'note_on' and msg.velocity > 0:
        note = msg.note
        velocity = msg.velocity
        # Scale the velocity to an appropriate multiplier value (0-1)
        amplitude = velocity / 127
        oscillators[note].mul = amplitude
        oscillators[note].freq = key_2freq(note)
        oscillators[note].out()
    elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
        note = msg.note
        oscillators[note].stop()


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
