# Distraction Shield Logging API
Welcome to the Distraction Shield Logging API

Requirements for Installation
============
- Python (2.7+)
- setuptools package (https://pypi.python.org/pypi/setuptools)

Usage
============
Download and extract the code. To run the server use the following commands:
```
sudo python setup.py install
export FLASK_APP="distraction-logging-api/main.py"
flask run
```

Pages
===========
At the moment, the flask-app support the following pages:
- http://localhost:5000/ for showing all data in a nice table
- http://localhost:5000/submit for posting new json data. The request must be specified as 'content-type': 'application/json'. For a post-example: see tests/post.py
