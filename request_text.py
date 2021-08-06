import requests
import OPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
api_url = 'http://8.16.250.212:4000/api/job'
myheaders = {'X-api-key': '0FF9258103494737B416217A10687F1B', 'Content-Type': 'application/json'}
myheaders2 = {'X-api-key': '516586FBB1084996BF54C339BD06A812', 'Content-Type': 'application/json'}
i = 2
n = 1
while i > n:
    while GPIO.input(12) == GPIO.LOW:
        time.sleep(0.01)
    if GPIO.input(12) == GPIO.HIGH:
        response = requests.post('http://8.16.250.212:4000/api/job', json={'command':'cancel'}, headers = myheaders)
        time.sleep(0.5)
        response2 = requests.post('http://8.16.250.212:4001/api/job', json={'command':'cancel'}, headers = myheaders)
        time.sleep(0.5)
        response3 = requests.post('http://8.16.250.212:4002/api/job', json={'command':'cancel'}, headers = myheaders2)
        print(response.status_code)
        print(response2.status_code)
        print(response3.status_code)
