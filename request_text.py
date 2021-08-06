import requests
import OPi.GPIO as GPIO
import time
import headers_lib as h_l
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
i = 2
n = 1
while i > n:
    while GPIO.input(12) == GPIO.LOW:
        time.sleep(0.01)
    response = requests.post('http://8.16.250.212:4000/api/job', json=h_l.Estop, headers = h_l.myheaders)
    response2 = requests.post('http://8.16.250.212:4001/api/job', json=h_l.Estop, headers = h_l.myheaders)
    response3 = requests.post('http://8.16.250.212:4002/api/job', json=h_l.Estop, headers = h_l.myheaders2)
    print(response.status_code)
    print(response2.status_code)
    print(response3.status_code)
    
