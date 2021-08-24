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
    print("-----------")
    print(json.dumps(request.form))
    print("-----------")
    form_data = request.form.to_dict()
    extra_data = json.loads(form_data['extra'])
    #name_data = extra_data['name']
    with open("printjob.txt", "w") as print_job:
        print_job.writelines("%s\n" % line for line in extra_data['name'])
        print_job.close()
    read_job = open("printjob.txt", "r")
    #while form_data['topic'] == 'Print Done':
    while GPIO.input(12) == GPIO.LOW:
            time.sleep(0.01)
            if GPIO.input(12) == GPIO.HIGH:
                #print(form_data['topic'])
                print(read_job)
                requests.post(f'http://8.16.250.212:4000/api/files/local/{read_job}', json={'command': 'select'}, headers={
                        'X-api-key': '0FF9258103494737B416217A10687F1B', 'Content-Type': 'application/json'})
                time.sleep(0.5)
                requests.post('http://8.16.250.212:4000/api/job', json={'command': 'start'}, headers={
                        'X-api-key': '0FF9258103494737B416217A10687F1B', 'Content-Type': 'application/json'})
    return 'JSON posted'


if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')
