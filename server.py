from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! <br><a href='/status'>Статус</a>"


@app.route("/status")
def status():
    return "Hello World!"


app.run()
