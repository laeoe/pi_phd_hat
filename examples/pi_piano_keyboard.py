from pi_phd_hat.midi_driver import MidiDriver
from pi_phd_hat.audio_driver import AudioPlayer

pi_synth = AudioPlayer()

def play_key(message):
    print(f"Received MIDI message: {message}")
    if message.type == 'note_on' and message.velocity > 0:
        print(f"Playing note {message.note}")
        pi_synth.play(message.note)


if __name__ == "__main__":
    midi_driver = MidiDriver("LPK25 mk2", message_callback=play_key)
    try:
        midi_driver.start_listening()
    finally:
        midi_driver.close_connection()