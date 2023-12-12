from pi_phd_hat.pi_piano import PiPiano
from pi_phd_hat.audio_driver import AudioPlayer
from pi_phd_hat.servo_driver import Level1, Level2, Level3
import time

# Define the gpio Pins used for the levels: 
# first 2 levels use the angles -25 and 65 degrees
# last level uses the angles -90 and 0 degrees


# Level3 = Level(14, 0, -90)

sequence = [64, 63, 64, 63, 64, 59, 62, 60, 57]
played = []
counter = 0

other_audio = AudioPlayer()

def check_played(note):
    global counter
    global sequence
    if counter == len(sequence):
        print("You won!")
        counter = 0
        return True
    
    elif note == sequence[counter]:
        print("Correct")
        counter += 1
        print(f"new counter value: {counter}")
        if counter == len(sequence):
            print("You won!")
            counter = 0
            return True
        return False
    
    else:
        print("Wrong")
        counter = 0
        other_audio.play_other("/home/pi/pi_phd_hat/assets/sounds/smb_bump.wav")
        return False

def callback_function(note: int):
    # This function will be called when a key is pressed, with the note number as argument
    print(f'callback function called, got note {note} of type {type(note)}')
    is_won = check_played(note)

    if is_won:
        print("You won!")
        other_audio.play_other(file_path="/home/pi/pi_phd_hat/assets/sounds/level_won.wav")
        Level1.open()
        Level2.open()
        Level3.open()

pi_piano = PiPiano(piano_callback=callback_function, verbose=False)
try:
    pi_piano.start()

except KeyboardInterrupt:
    pi_piano.close()