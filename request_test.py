import OPi.GPIO as GPIO
import time
import commands
import requests

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)

while 2>1:
    while GPIO.input(12) == GPIO.LOW:
        time.sleep(0.01)
    if GPIO.input(12)==GPIO.HIGH:
        commands.stopcommand()
    
