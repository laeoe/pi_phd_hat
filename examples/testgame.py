from pi_phd_hat.pi_piano import PiPiano
from pi_phd_hat.servo_driver import Level

# Define the gpio Pins used for the levels: 
# first 2 levels use the angles -25 and 65 degrees
# last level uses the angles -90 and 0 degrees

Level3 = Level(14, 0, -90)

def callback_function(note: int):
    # This function will be called when a key is pressed, with the note number as argument
    print(f'callback function called, got note {note} of type {type(note)}')
    if note == 60:
        Level3.open()

pi_piano = PiPiano(piano_callback=callback_function, verbose=False)
try:
    pi_piano.start()

except KeyboardInterrupt:
    pi_piano.close()