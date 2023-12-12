# Servo driver for rasberry pi 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


class ServoDriver:
    def __init__(self, pin, min_angle=0, max_angle=180, min_duty_cycle=2.5, max_duty_cycle=12.5):
        self.pin = pin
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.min_duty_cycle = min_duty_cycle
        self.max_duty_cycle = max_duty_cycle
        self.current_angle = 0
        self.current_duty_cycle = 0
        self.pwm = None

    def start(self):
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)
        self.pwm.start(self.min_duty_cycle)
        self.set_angle(self.min_angle)

    def set_angle(self, angle):
        if angle < self.min_angle:
            angle = self.min_angle
        elif angle > self.max_angle:
            angle = self.max_angle
        self.current_angle = angle
        duty_cycle = self.min_duty_cycle + (self.max_duty_cycle - self.min_duty_cycle) * angle / 180
        self.current_duty_cycle = duty_cycle
        self.pwm.ChangeDutyCycle(duty_cycle)

    def close(self):
        self.pwm.stop()
        GPIO.cleanup()
        print("Servo driver stopped")

    

if __name__ == "__main__":
    servo_driver = ServoDriver(14)
    servo_driver.start()
    try:
        while True:
            for angle in range(0, 180, 10):
                servo_driver.set_angle(angle)
                time.sleep(0.1)
            for angle in range(180, 0, -10):
                servo_driver.set_angle(angle)
                time.sleep(0.1)
    except KeyboardInterrupt:
        servo_driver.close()