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

def process_midi_message(msg):
    if msg.type == 'note_on' and msg.velocity > 0:
        note = msg.note
        velocity = msg.velocity
        # Scale the velocity to an appropriate multiplier value (0-1)
        amplitude = velocity / 127
    elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
        note = msg.note
        amplitude = 0

    return (note, amplitude, 0)

if __name__ == "__main__":
    print("Reading MIDI input. Press Ctrl+C to stop.")
    for msg in midi_input:
        print(process_midi_message(msg))