import requests
import OPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)

while GPIO.input(12) == GPIO.LOW:
    time.sleep(0.01)
if GPIO.input(12) == GPIO.HIGH:
    requests.post('8.16.250.212:4000/api/job', json={'command': 'M112'},headers= {'X-api-key': '0FF9258103494737B416217A10687F1B', 'Content-Type': 'application/json'})

