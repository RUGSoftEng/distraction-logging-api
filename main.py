from flask import Flask, render_template, request
from database import session_scope, Log
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

with session_scope() as db_session:
    x = db_session.query(Log).count() + 1
   

# show all data
@app.route('/')
def index():
    with session_scope() as db_session:
        data = db_session.query(Log).all()
        # when using the object retrieved from the database outside
        # the with-scope, use the line below to extract the data.
        db_session.expunge_all()
        print data 

    return render_template('index.html', data=data)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    global x
    data = request.get_json()
    for i in data:
        entry = Log(id=x, userID=i['id'], event=i['event'], value=i['value'], time=i['time'])
        with session_scope() as db_session:
            db_session.add(entry)
        x += 1
    return "ok" 


if __name__ == '__main__':
    app.run(debug=True)
