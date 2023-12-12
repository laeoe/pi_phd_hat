from gpiozero import Servo
from time import sleep

servo = Servo(14, min_pulse_width = 0.0005, max_pulse_width = 0.0025)

# while True:
#     servo.min()
#     sleep(1)
#     # servo.mid()
#     sleep(1)
#     servo.max()
#     sleep(2)
#     print('again')


while True:
    # enter an input angle
    angle = input("Enter an angle between -90 and 90 degrees: ")
    # convert the angle to a float
    angle = float(angle)
    # convert the angle to a value between -1 and 1
    angle = angle / 90
    # set the servo
    servo.value = angle
    # wait for the servo to get there
    sleep(1)