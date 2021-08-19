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

@app.route('/Posting', methods=['POST'])
def Posting():
    form_data = request.form.to_dict()
    extra_data = json.loads(form_data['extra'])
    name_data = extra_data['name']
    url_var = f'http://8.16.250.212:4000/api/files/{name_data}'
    print(url_var)
    print(form_data['topic'])
    print(extra_data['name'])
    # while form_data['topic'] == 'Print Done':
    #     while GPIO.input(12) == GPIO.LOW:
    #         time.sleep(0.01)
    #         print("waiting for button")
    #     if GPIO.input(12) == GPIO.HIGH:
    #         requests.post (f'http://8.16.250.212:4000/api/files/{name_data}', json = {'command': 'select', 'print': 'true'}, headers = {'X-api-key': '0FF9258103494737B416217A10687F1B', 'Content-Type': 'application/json'})
    #         print("button pressed")
    return 'JSON posted'


if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')
