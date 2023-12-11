from src.midi_driver import *


try: 
    print("Reading MIDI input. Press Ctrl+C to stop.")
    for msg in midi_input:
        print(process_midi_message(msg))

except KeyboardInterrupt:
    print("Exiting...")