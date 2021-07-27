import OPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
GPIO.setup(7,GPIO.OUT)
i=2
n=0
while i > n:
    while GPIO.input(12) == GPIO.LOW:
        time.sleep(0.01)
    if GPIO.input(12) == GPIO.HIGH:
        print("input is High")
    GPIO.output(7, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(7, GPIO.LOW)
    print("pressed")
GPIO.cleanup()
