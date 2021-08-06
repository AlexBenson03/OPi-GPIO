import OPi.GPIO as GPIO
import time
import stop
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
i = 2
n = 1
while i > n:
    while GPIO.input(12) == GPIO.LOW:
        time.sleep(0.01)
    print("button pressed")
    stop.stopcommd
