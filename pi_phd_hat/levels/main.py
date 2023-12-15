import subprocess
from pi_phd_hat.audio_driver import AudioPlayer


other_audio = AudioPlayer()

path_level1 = "/home/pi/pi_phd_hat/pi_phd_hat/levels/Level1.py"
path_level2 = "/home/pi/pi_phd_hat/pi_phd_hat/levels/Level2.py"
path_level3 = "/home/pi/pi_phd_hat/pi_phd_hat/levels/Level3.py"

path_hat_won = "/home/pi/pi_phd_hat/assets/sounds/hat_won.wav"
# path_level_won = "/home/pi/pi_phd_hat/assets/sounds/smb_powerup.wav"
sample_rate_other = 22000


def start_level(path_to_level):
    try:
        process = subprocess.Popen(['python', path_to_level])
        process.wait()
    except KeyboardInterrupt:
        pass
    print("\n###############\nLevel Ended, starting Next...\n###############\n")



if __name__ == "__main__":
    while True:
        try: 
            start_level(path_level1)
            start_level(path_level2)
            start_level(path_level3)

            # Fall back to the piano: 
            print("\n\n###############\nGame Won returning to Pi Piano\n###############\n\n")
            other_audio.play_other(path_hat_won, sample_rate_other)

            example_piano_path = "/home/pi/pi_phd_hat/examples/pi_piano.py"
            start_level(example_piano_path)
        except KeyboardInterrupt:
            pass
        endless_loop = input("Do you want to play again? (y/n)")
        if endless_loop == "n":
            break
        else:
            pass
        
