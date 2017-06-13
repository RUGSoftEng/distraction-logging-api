from flask import Flask, render_template, request
from .database import session_scope, Log
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

# Query to get size of the database, this is used as a primary key
with session_scope() as db_session:
    dbSize = db_session.query(Log).count() + 1
   

# show all data
@app.route('/')
def index():
    with session_scope() as db_session:
        data = db_session.query(Log).all()
        data = data[-50:]
        # when using the object retrieved from the database outside
        # the with-scope, use the line below to extract the data.
        db_session.expunge_all()
    return render_template('index.html', data=data)


""" Receives a list of JSON objects, with one JSON object corresponding to one log (change in options, a redirect etc).
We then iterate through these objects and enter them into the database. Each user sends a list of their logs once a day """ 
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    global dbSize
    data = request.get_json()
    for i in data:
        entry = Log(id=dbSize, userID=i['id'], event=i['event'], trigger=i['trigger'], value=i['value'], time=i['time'], type=i['type'])
        with session_scope() as db_session:
            db_session.add(entry)
        dbSize += 1
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
