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


@app.route('/Posting', methods=['POST', 'GET', 'PUT'])
def Posting():
   form_data = request.form.to_dict()
   extra_data = json.loads(form_data['extra'])
   name_data = extra_data['name']
   print_name = [extra_data['name']]
   with open("printjob.txt", "w") as printjob:
        printjob.writelines("%s\n" % line for line in print_name)
   printjob.close()
   printjob = open("printjob.txt", "r")
   print(printjob.read())
   while form_data['topic'] == 'Print Done':
       while GPIO.input(12) == GPIO.LOW:
           time.sleep(0.01)
       if GPIO.input(12) == GPIO.HIGH:
          requests.post (f'http://8.16.250.212:4000/api/files/local/{name_data}', json = {'command': 'select', 'print': 'true'}, headers = {'X-api-key': '0FF9258103494737B416217A10687F1B', 'Content-Type': 'application/json'})
       break
   return 'JSON posted'


if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')
