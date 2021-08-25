from flask import Flask, request
import json
import time
import OPi.GPIO as GPIO
import requests


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/Posting', methods=['POST', 'GET'])
def Posting():
    while GPIO.input(12) == GPIO.LOW:
        print('button not pressed')
        time.sleep(0.01)
        if GPIO.input(12) == GPIO.HIGH:
            print('buttton pressed')
            req_data = requests.get('http://8.16.250.212:4000//api/job', headers={
                     'X-api-key': '0FF9258103494737B416217A10687F1B', 'Content-Type': 'application/json'})
            name_data = json.loads(req_data.text)
            print(name_data)
            job_data = name_data['job']
            print(job_data)
            file_data = job_data['file']
            print(file_data)
            print_job = file_data['name']
            print(print_job)
            requests.post(f'http://8.16.250.212:4000/api/files/local/{print_job}', json={'command': 'select'}, headers={
                         'X-api-key': '0FF9258103494737B416217A10687F1B', 'Content-Type': 'application/json'})
            time.sleep(0.5)
            requests.post('http://8.16.250.212:4000/api/job', json={'command': 'start'}, headers={
                         'X-api-key': '0FF9258103494737B416217A10687F1B', 'Content-Type': 'application/json'})
    return 'JSON posted'


if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')
