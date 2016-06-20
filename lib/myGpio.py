import RPi.GPIO as GPIO

MOTOR_L_F = 35
MOTOR_L_B = 36
MOTOR_R_F = 37
MOTOR_R_B = 38

def setup():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(MOTOR_L_F, GPIO.OUT)
    GPIO.setup(MOTOR_L_B, GPIO.OUT)
    GPIO.setup(MOTOR_R_F, GPIO.OUT)
    GPIO.setup(MOTOR_R_B, GPIO.OUT)

    GPIO.output(MOTOR_L_F, False)
    GPIO.output(MOTOR_L_B, False)
    GPIO.output(MOTOR_R_F, False)
    GPIO.output(MOTOR_R_B, False)

def write(pin, state):
    """
    Write output GPIO pin to state MAKE SURE pin is setup before use
    @param int pin
    @param bool state
    """
    print("GPIO WRITE", pin, state)
    GPIO.output(pin, state)

import atexit
@atexit.register
def shutdown():
    """
    Shutdown GPIO
    """
    print("My shutdown GPIO")
    GPIO.cleanup()
