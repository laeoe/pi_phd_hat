import mido

class MidiDriver:
    def __init__(self, device_name, message_callback=None):
        self.device_name = device_name
        self.message_callback = message_callback
        self.midi_input = self._connect_to_device()

    def _connect_to_device(self):
        for input_name in mido.get_input_names():
            print(f"Found MIDI input: {input_name}")
            if self.device_name in input_name:
                return mido.open_input(input_name)
        raise Exception(f"MIDI Keyboard '{self.device_name}' not found.")

    def start_listening(self):
        """Starts listening for MIDI messages and uses the callback when a message is received."""
        try:
            while True:
                for msg in self.midi_input.iter_pending():
                    if self.message_callback:
                        self.message_callback(msg)
        except KeyboardInterrupt:
            print("Stopping MIDI input listening.")

    def close_connection(self):
        if self.midi_input:
            self.midi_input.close()
            print(f"Connection to '{self.device_name}' closed.")
