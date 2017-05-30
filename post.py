"""
Run this file if you want to send some data to the server and tests if it works.
"""

import requests
import json

url = 'http://127.0.0.1:5000/submit'
headers = {'content-type': 'application/json'}
data = {"id": "4",
        "event": "changed GreenToRedSlider",
        "value": "23",
        "time": "2017-05-29T15:20:28.661Z"}

response = requests.post(url, data=json.dumps(data), headers=headers)
