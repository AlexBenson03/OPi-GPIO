import OPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
GPIO.setup(7,GPIO.OUT)
while GPIO.input(12) == GPIO.LOW:
    time.sleep(0.01)
x = 0
if x < 3:
    GPIO.output(7, GPIO.HIGH)
    time.sleep(1)
    GPIO.OUTPUT(7, GPIO.LOW)
    x = x + 1
print("pressed")
GPIO.cleanup()
