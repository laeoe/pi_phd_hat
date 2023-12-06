import mido
from pyo import *

# Initialize Pyo server
s = Server().boot()
s.start()

# Function to convert MIDI note numbers to frequency
def midi_to_freq(note):
    a = 440  # frequency of A (common value is 440Hz)
    return (a / 32) * (2 ** ((note - 9) / 12))

# Create a sine wave oscillator but don't play it yet
osc = Sine(freq=440, mul=0.1).out()
osc.stop()

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
        osc.freq = midi_to_freq(msg.note)
        osc.out()
    elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
        # Stop the oscillator
        osc.stop()

# Main loop to read MIDI messages
try:
    print("Reading MIDI input. Press Ctrl+C to stop.")
    for msg in midi_input:
        process_midi_message(msg)
except KeyboardInterrupt:
    print("Exiting...")

# Clean up
s.stop()
