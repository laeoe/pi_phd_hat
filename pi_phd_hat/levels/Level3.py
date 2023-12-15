# Main programme: 

from pi_phd_hat.pi_piano import PiPiano
from pi_phd_hat.play_correct_sequence import Play_correct_sequence
from pi_phd_hat.servo_driver import Level_Servo

song_topolino = [[64], [62], [64], [62], [64], [65], [64], [60], [60], [60], [60]] 
# make the same sequence backwards 
song_topolino_backwards = song_topolino[::-1]

# add the second octave
song_topolino_dual = [[64, 76], [62, 74], [64, 76], [62, 74], [64, 76], [65, 77], [64, 76], [60, 72], [60, 72], [60, 72], [60, 72]]




def play_level(level, servo):
    try: 
        level.start()
    except KeyboardInterrupt:
        pass
    servo.open()
    exit()

# level1 = Play_correct_sequence(song_topolino)
# level2 = Play_correct_sequence(song_topolino_backwards)
level3 = Play_correct_sequence(song_topolino_dual)


def main():
    Level1_Servo = Level_Servo(14, 65, -25, init_state = "open")
    Level2_Servo = Level_Servo(15, 65, -25, init_state = "open")
    Level3_Servo = Level_Servo(23, -90, 0, init_state = "closed")
    print("\n ###############\n Starting Level 3\n ###############\n")
    play_level(level3, Level3_Servo)

if __name__ == "__main__":
    main()