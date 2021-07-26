import OPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(6, GPIO.OUT)
GPIO.output(6,GPIO.High)
time.sleep(1)
GPIO.output(6,GPIO.LOW)
GPIO.cleanup()
