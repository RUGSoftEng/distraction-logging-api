from flask import Flask, render_template, request
from .database import session_scope, Log
app = Flask(__name__)


# show all data
@app.route('/')
def index():
    with session_scope() as db_session:
        data = db_session.query(Log).all()
        # when using the object retrieved from the database outside
        # the with-scope, use the line below to extract the data.
        db_session.expunge_all()

    return render_template('index.html', data=data)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    data = request.get_json()
    entry = Log(id=data['id'], event=data['event'], value=data['value'], time=data['time'])
    with session_scope() as db_session:
        db_session.add(entry)
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
