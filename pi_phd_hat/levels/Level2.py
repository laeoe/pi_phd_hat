# Main programme: 

from pi_phd_hat.pi_piano import PiPiano
from pi_phd_hat.play_correct_sequence import Play_correct_sequence
from pi_phd_hat.servo_driver import Level_Servo

song_topolino = [[64], [62], [64], [62], [64], [65], [64], [60], [60], [60], [60]] 
# make the same sequence backwards 
song_topolino_backwards = song_topolino[::-1]


Level1_Servo = Level_Servo(14, 65, -25, init_state = "open")
Level2_Servo = Level_Servo(15, 65, -25, init_state = "closed")
Level3_Servo = Level_Servo(23, -90, 0, init_state = "closed")


def play_level(level, servo):
    try: 
        level.start()
    except KeyboardInterrupt:
        pass
    servo.open()
    exit()

# level1 = Play_correct_sequence(song_topolino)
level2 = Play_correct_sequence(song_topolino_backwards)
# level3 = Play_correct_sequence([[61]])


def test_main():
    str1 = "\n\n\n\n\n\n##############################\n"
    str2 = "\n##############################\n\n\n\n\n\n"
    print(str1)
    print("     Starting level 2")
    print(str2)
    play_level(level2, Level2_Servo)

if __name__ == "__main__":
    test_main()