from pi_phd_hat.midi_driver import MidiDriver
from pi_phd_hat.audio_driver import AudioPlayer

class PiPiano():
    def __init__(self, piano_callback = None):
        self.pi_synth = AudioPlayer()
        self.midi_driver = MidiDriver("LPK25 mk2", message_callback=self.play_key)
        self.piano_callback = piano_callback

    def play_key(self, message):
        # plays the pressed key through the speaker and returns the number of the note as int
        # print(f"Received MIDI message: {message}")
        if message.type == 'note_on' and message.velocity > 0:
            # print(f"Playing note {message.note}")
            self.pi_synth.play(message.note)
            if self.piano_callback:
                self.piano_callback(message.note)

    def start(self):
        print("Pi Piano started")
        try: 
            self.midi_driver.start_listening()
        finally:
            self.midi_driver.close_connection()
            self.pi_synth.close()


if __name__ == "__main__":
    pi_piano = PiPiano()
    pi_piano.start()