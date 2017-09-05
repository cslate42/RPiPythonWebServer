"""
Basic IO
reference https://sourceforge.net/p/raspberry-gpio-python/wiki/pwmPins/
"""

import atexit
import RPi.GPIO as GPIO

MOTOR_L_F = 35
MOTOR_L_B = 36
MOTOR_R_F = 37
MOTOR_R_B = 38
LED_TEST = 3

pwmPins = {}

def setup():
    """
    Setup the raspberry pi pins and interrupts
    """
    print "-------------------------SETTING UP GPIO----------------------------"
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(MOTOR_L_F, GPIO.OUT)
    GPIO.setup(MOTOR_L_B, GPIO.OUT)
    GPIO.setup(MOTOR_R_F, GPIO.OUT)
    GPIO.setup(MOTOR_R_B, GPIO.OUT)
    GPIO.setup(LED_TEST, GPIO.OUT)
    # GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

    GPIO.output(MOTOR_L_F, False)
    GPIO.output(MOTOR_L_B, False)
    GPIO.output(MOTOR_R_F, False)
    GPIO.output(MOTOR_R_B, False)
    GPIO.output(LED_TEST, False)
    pwmPins.clear()
    return

def write(pin, state):
    """
    Write output GPIO pin to state MAKE SURE pin is setup before use
    @param int pin
    @param bool state
    """
    if GPIO.getmode() is None:
        return False
    # print("GPIO WRITE", pin, state, gpioState)
    gpioState = GPIO.HIGH if state is True or state == 1 or state == "1" else GPIO.LOW
    if pwmPins.get(pin) is None:
        GPIO.output(pin, gpioState)
        # pwmPins.get(pin).stop()
    else:
        GPIO.output(pin, gpioState)
    return

def pwmPinsUpdate(pin, freq, dutyCycle):
    """
    Start pwmPins on pin
    @param int pin
    @param float freq
        in Hz
    @param float dutyCycle
        (0.0 <= dc <= 100.0)
    """
    # print("pwmPinsUpdate", pin, freq, dutyCycle, pwmPins.get(pin))
    if pwmPins.get(pin) is None:
        pwmPins[pin] = GPIO.PWM(pin, freq)
        pwmPins.get(pin).start(dutyCycle)
    else:
        pwmPins.get(pin).ChangeDutyCycle(dutyCycle)
        pwmPins.get(pin).ChangeFrequency(freq)

    return

def pwmPinsStop(pin):
    """
    Stop pwmPins then remove from dictionary
    @param int pin
    """
    if pwmPins.get(pin):
        # print("STOPPING", pin)
        pwmPins.get(pin).stop()
        del pwmPins[pin]
    return

def reset():
    """
    Attempt to reset GPIO pins
    Occationally had problems with resources not being freed up
    """
    GPIO.cleanup()
    setup()
    return

@atexit.register
def shutdown():
    """
    Shutdown GPIO and cleanup pin configs
    """
    print "My shutdown GPIO"
    GPIO.cleanup()
