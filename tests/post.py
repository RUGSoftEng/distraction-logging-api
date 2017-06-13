"""
Run this file if you want to send some data to the server and tests if it works.
"""

import requests
import json

url = 'http://localhost:5000/submit'
headers = {'content-type': 'application/json'}
data = [
        {"id": "30",
        "event": "Test",
        "trigger": "switch",
        "value": "moretest",
        "time": "2017-05-29T15:20:28.661Z",
        "type": "test"},
        {"id": "40",
        "event": "Test",
        "trigger": "switch",
        "value": "23",
        "time": "2017-05-29T15:20:28.661Z",
        "type": "hihi"}
       ]

response = requests.post(url, data=json.dumps(data), headers=headers)
