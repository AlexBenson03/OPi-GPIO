import requests
import headers_lib as h_l
def stopcommd():
    r0 = requests.post('http://8.16.250.212:4000/api/job', json={'command': 'pause', 'action':'toggle'}, headers = h_l.myheaders0)
    r1 = requests.post('http://8.16.250.212:4001/api/job', json={'command': 'pause', 'action':'toggle'}, headers = h_l.myheaders0)
    r2 = requests.post('http://8.16.250.212:4002/api/job', json={'command': 'pause', 'action':'toggle'}, headers = h_l.myheaders1)
    print(r0.status_code)
    print(r1.status_code)
    print(r2.status_code)
