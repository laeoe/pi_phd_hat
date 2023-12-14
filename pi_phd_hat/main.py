# Main programme: 

from pi_phd_hat.pi_piano import PiPiano
from pi_phd_hat.play_correct_sequence import Play_correct_sequence
from pi_phd_hat.servo_driver import Level1_Servo, Level2_Servo, Level3_Servo, Level_Servos

song_topolino = [[76], [74], [76], [74], [76], [77], [76], [72], [72], [72], [72]] 

test_song = [[60, 72], [62, 74], [64, 76]]




def play_level(level, servo):
    try: 
        level.start()
    except KeyboardInterrupt:
        pass
    servo.open()

level1 = Play_correct_sequence(test_song)
level2 = Play_correct_sequence(song_topolino)
level3 = Play_correct_sequence([[61]])


def test_main():
    print("Testing a complete run")
    play_level(level1, Level1_Servo)
    play_level(level2, Level2_Servo)
    play_level(level3, Level3_Servo)

if __name__ == "__main__":
    test_main()