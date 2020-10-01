from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! <br><a href='/status'>Статус</a>"


@app.route("/status")
def status():
    status = True
    name = "my_messenger"
    time = datetime.now()
    return "Я смог запустить свой сервер: " + name + " для курса!"


app.run()
