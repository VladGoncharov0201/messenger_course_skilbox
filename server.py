from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "Сервер запущен! <br><a href='/status'>Статус</a>"


@app.route("/status")
def status():
    return {'status': True,
            'name': "my_messenger",
            'time': datetime.now()
            }


app.run(debug=True)
