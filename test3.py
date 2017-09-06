import RPi.GPIO as GPIO
PWM_LED = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWM_LED, GPIO.OUT)

p = GPIO.PWM(PWM_LED, 50)
p.start(0)
p.ChangeDutyCycle(100)
try:
    while True:
        a = 0
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

# import time
# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(12, GPIO.OUT)
#
# p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
# p.start(0)
# try:
#     while 1:
#         for dc in range(0, 101, 5):
#             p.ChangeDutyCycle(dc)
#             time.sleep(0.1)
#         for dc in range(100, -1, -5):
#             p.ChangeDutyCycle(dc)
#             time.sleep(0.1)
# except KeyboardInterrupt:
#     pass
# p.stop()
# GPIO.cleanup()
