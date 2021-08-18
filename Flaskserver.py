from flask import Flask, request
import json
import flaskserverbutton

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/Posting', methods=['POST'])
def Posting():
    form_data = request.form.to_dict()
    extra_data = json.loads(form_data['extra'])
    print(form_data['topic'])
    print(extra_data['name'])
    while form_data['topic'] == 'Print Done':
        flaskserverbutton.restartbutton

    return 'JSON posted'


if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')
