from flask import Flask
import time
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Сервер запущен! <br><a href='/status'>Статус</a>"


@app.route("/status")
def status():
    return json.dumps({'status': True,
                       'name': "my_messenger",
                       'time': time.ctime()
                       })


app.run(debug=True)
