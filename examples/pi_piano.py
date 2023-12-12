from pi_phd_hat.pi_piano import PiPiano

def callback_function(note: int):
    # This function will be called when a key is pressed, with the note number as argument
    print(f'callback function called, got note {note} of type {type(note)}')

pi_piano = PiPiano(piano_callback=callback_function, verbose=False)
try:
    pi_piano.start()

except KeyboardInterrupt:
    pi_piano.close()