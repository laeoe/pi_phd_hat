from gpiozero import Servo
from time import sleep

# servo = Servo(14, min_pulse_width = 0.0005, max_pulse_width = 0.0025)

#top: 
# pin nr: 
# angle open
# angle closed 

#last 
# angle open 0
# angle closed -90

# while True:
#     # enter an input angle
#     servo.value = None
#     angle = input("Enter an angle between -90 and 90 degrees: ")
#     # convert the angle to a float
#     angle = float(angle)
#     # convert the angle to a value between -1 and 1
#     angle = angle / 90
#     # set the servo
#     servo.value = angle
#     # wait for the servo to get there
#     sleep(1)
#     servo.value = None


class Level: 
    def __init__(self, pin_nr, angle_open, angle_closed):
        self.pin_nr = pin_nr
        self.angle_open = angle_open
        self.angle_closed = angle_closed
        self.servo = Servo(pin_nr, min_pulse_width = 0.0005, max_pulse_width = 0.0025)
        self.servo.value = None
        self.state = "closed"
        self.close()

    def angle_2_value(self, angle):
        return angle / 90
    
    def open(self):
        self.servo.value = self.angle_2_value(self.angle_open)
        sleep(1)
        self.servo.value = None
        self.state = "open"

    def close(self):
        self.servo.value = self.angle_2_value(self.angle_closed)
        sleep(1)
        self.servo.value = None
        self.state = "closed"

    

