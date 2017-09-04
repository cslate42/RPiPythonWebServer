# https://sourceforge.net/p/raspberry-gpio-python/wiki/pwmPins/


#===============================+START SETUP+=============================
MOTOR_L_F = 35
MOTOR_L_B = 36
MOTOR_R_F = 37
MOTOR_R_B = 38
LED_TEST = 3

pwmPins = {}

def setup():
    print("-------------------------_SETTING UP GPIO_----------------------------")
    return

setup()

#===============================+END SETUP+=============================
def write(pin, state):
    """
    Write output GPIO pin to state MAKE SURE pin is setup before use
    @param int pin
    @param bool state
    """
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
    return

def pwmPinsStop(pin):
    """
    Stop pwmPins then remove from dictionary
    @param int pin
    """
    return

def reset():
    setup()
    return

import atexit
@atexit.register
def shutdown():
    """
    Shutdown GPIO
    """
    print("My shutdown GPIO")
