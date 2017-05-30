# flask-api
A simple REST-webserver for logging information.

Usage
============
Download and extract the code and run the flask-application. If you have trouble running a flask-application, see: http://flask.pocoo.org/docs/0.12/quickstart/

Pages
===========
At the moment, the flask-app support the following pages:
- http://localhost:5000/ for showing all data in a nice table
- http://localhost:5000/submit for posting new json data. The request must be specified as 'content-type': 'application/json'. For a post-example: see post.py
