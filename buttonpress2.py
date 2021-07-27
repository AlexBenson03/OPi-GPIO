import OPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
while GPIO.input(12) == GPIO.LOW:
    time.sleep(0.01)
