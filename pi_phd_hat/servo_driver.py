from gpiozero import Servo
from time import sleep

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


class Servo_Tester:
    def __init__(self, pin_nr):
        self.pin_nr = pin_nr
        self.servo = Servo(pin_nr, min_pulse_width = 0.0005, max_pulse_width = 0.0025)
        self.servo.value = None
        self.state = "closed"

    def angle_2_value(self, angle):
        return angle / 90
    
    def start_cmd_input_dialog(self):
        while True:
            angle = int(input("Enter a new input angle, escape to quit: "))
            if angle == "escape":
                break
            
            if angle > abs(90):
                print("Angle must be between -90 and 90 degrees")
                continue


            servo.value = self.angle_2_value(float(angle))
            sleep(1)
            servo.value = None


Level1 = Level(14, 65, -25)
Level2 = Level(15, 65, -25)
Level3 = Level(23, 0, -90)



Levels = [Level1, Level2, Level3]

if __name__ == "__main__":
    # servo = Servo_Tester(14)
    # servo.start_cmd_input_dialog()
    print("Testing servo driver")
    while True:
        for level in Levels:
            print(f"Testing level {level.pin_nr}")
            level.open()
            sleep(1)
            level.close()
            sleep(1)

