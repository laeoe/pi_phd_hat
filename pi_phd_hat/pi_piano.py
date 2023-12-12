from pi_phd_hat.midi_driver import MidiDriver
from pi_phd_hat.audio_driver import AudioPlayer

class PiPiano():
    def __init__(self, piano_callback = None, verbose = True):
        self.pi_synth = AudioPlayer()
        self.midi_driver = MidiDriver("LPK25 mk2", message_callback=self.play_key)
        self.piano_callback = piano_callback
        self.verbose = verbose

    def play_key(self, message):
        # plays the pressed key through the speaker and returns the number of the note as int
        # print(f"Received MIDI message: {message}")
        if message.type == 'note_on' and message.velocity > 0:
            print(message.note) if self.verbose else None
            self.pi_synth.play(message.note)
            if self.piano_callback:
                self.piano_callback(message.note)

    def play_other(self, file_path):
        print(f"Playing file {file_path}")
        self.pi_synth.play_other(file_path)

    def start(self):
        print("Pi Piano started")
        try: 
            self.midi_driver.start_listening()
        finally:
            self.midi_driver.close_connection()
            self.pi_synth.close()

    def close(self):
        print("Exiting the pi piano")
        self.midi_driver.close_connection()
        self.pi_synth.close()


if __name__ == "__main__":
    def print_key(note):
        print(f'callback function called, got note {note} of type {type(note)}')

    pi_piano = PiPiano(piano_callback=print_key, verbose=False)
    pi_piano.start()