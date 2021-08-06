import OPi.GPIO as GPIO
import time
from commands import *

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)

while GPIO.input(12) == GPIO.LOW:
    time.sleep(0.01)
if GPIO.input(12)==GPIO.HIGH:
    stopcommand()
