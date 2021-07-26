import OPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(6, GPIO.OUT)
print("Led on")
GPIO.output(6,GPIO.High)
time.sleep(1)
print("LED off")
GPIO.output(6,GPIO.LOW)
