from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

#how to run:
#set FLASK_APP=try_flask.py
#flask run