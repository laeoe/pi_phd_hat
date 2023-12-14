import mido

class MidiDriver:
    def __init__(self, device_name, message_callback=None):
        self.device_name = device_name
        self.message_callback = message_callback
        self.midi_input = self._connect_to_device()
        self.is_listening = False

    def _connect_to_device(self):
        for input_name in mido.get_input_names():
            print(f"Found MIDI input: {input_name}")
            if self.device_name in input_name:
                return mido.open_input(input_name)
        raise Exception(f"MIDI Keyboard '{self.device_name}' not found.")

    def start_listening(self):
        """Starts listening for MIDI messages and uses the callback when a message is received."""
        self.is_listening = True
        try:
            while self.is_listening:
                for msg in self.midi_input:
                    if self.message_callback:
                        self.message_callback(msg)
        except KeyboardInterrupt:
            # print("Stopping MIDI input listening.")
            pass
        finally:
            self.close()
        # print("Stopped listening for MIDI messages")

    def stop_listening(self):
        """Stops listening for MIDI messages."""
        self.is_listening = False

    def close(self):
        """Closes the connection to the MIDI device."""
        self.is_listening = False
        if self.midi_input:
            self.midi_input.close()
        # print(f"closed connection to '{self.device_name}'.")



if __name__ == "__main__":
    def callback(msg):
        print(msg)

    midi_driver = MidiDriver(device_name="LPK25 mk2", message_callback=callback)
    midi_driver.start_listening()
    midi_driver.close()