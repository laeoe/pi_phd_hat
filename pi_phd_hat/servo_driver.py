from gpiozero import Servo
from time import sleep

servo = Servo(14, min_pulse_width = 0.0005, max_pulse_width = 0.0025)

while True:
    servo.min()
    sleep(1)
    # servo.mid()
    sleep(1)
    servo.max()
    sleep(2)
    print('again')

