# Main programme: 

from pi_phd_hat.pi_piano import PiPiano
from pi_phd_hat.play_correct_sequence import Play_correct_sequence
from pi_phd_hat.servo_driver import Level_Servo

song_topolino = [[76], [74], [76], [74], [76], [77], [76], [72], [72], [72], [72]] 
# make the same sequence backwards 
song_topolino_backwards = song_topolino[::-1]


test_song = [[60, 72], [62, 74], [64, 76]]


Level1_Servo = Level_Servo(14, 65, -25, init_state = "closed")
Level2_Servo = Level_Servo(15, 65, -25, init_state = "closed")
Level3_Servo = Level_Servo(23, -90, 0, init_state = "closed")


def play_level(level, servo):
    try: 
        level.start()
    except KeyboardInterrupt:
        pass
    servo.open()
    exit()

level1 = Play_correct_sequence(song_topolino)
# level2 = Play_correct_sequence(song_topolino_backwards)
# level3 = Play_correct_sequence([[61]])


def test_main():
    print("\n ###############\n Starting Level 1\n ###############\n")
    play_level(level1, Level1_Servo)

if __name__ == "__main__":
    test_main()