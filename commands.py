import requests
def stopcommd():
    r0 = requests.post('http://8.16.250.212:4000/api/job', json={'command': 'cancel'}, headers = {'X-api-key': '0FF9258103494737B416217A10687F1B', 'Content-Type': 'application/json'})
    r1 = requests.post('http://8.16.250.212:4001/api/job', json={'command': 'cancel'}, headers = {'X-api-key': '0FF9258103494737B416217A10687F1B', 'Content-Type': 'application/json'})
    r2 = requests.post('http://8.16.250.212:4002/api/job', json={'command': 'cancel'}, headers = {'X-api-key': '516586FBB1084996BF54C339BD06A812', 'Content-Type': 'application/json'})
    
    print(r0.status_code)
    print(r1.status_code)
    print(r2.status_code)
