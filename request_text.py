import requests
import OPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
api_url = 'http://8.16.250.212:4000/api/printer'
myheaders = {'X-api-key': '0FF9258103494737B416217A10687F1B', 'Content-Type': 'application/json'}
i = 2
n = 1
while i > n:
    while GPIO.input(12) == GPIO.LOW:
        time.sleep(0.01)
    if GPIO.input(12) == GPIO.HIGH:
        response = requests.post(api_url, json={'command':'start'}, headers = myheaders)
        print(response.status_code)
