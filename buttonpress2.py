import OPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
i=2
n=0
while i > n:
    GPIO.setup(12, GPIO.IN)
    GPIO.setup(7,GPIO.OUT)
    while GPIO.input(12) == GPIO.LOW:
        time.sleep(0.01)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(7, GPIO.LOW)
    print("pressed")
    GPIO.cleanup()
