from flask import Flask, Response, request
from datetime import datetime
import time

app = Flask(__name__)
db = [

]


@app.route("/")
def hello():
    return "Сервер запущен! <br><a href='/status'>Статус</a>"


@app.route("/status")
def status():
    dn = datetime.now()
    return {'status': True,
            'name': "my_messenger",
            'time': str(dn)
            }


@app.route("/send_message", methods=['POST'])
def send_message():
    data = request.json
    if not isinstance(data, dict):
        return Response('not json', 400)

    text = data.get('text')
    author = data.get('author')

    if isinstance(author, str):
        db.append({
            'text': text,
            'author': author,
            'time': time.time()
        })
        return Response('ok')
    else:
        return Response('wrong format', 400)


@app.route("/get_message")
def get_message():
    after = request.args.get('after', '0')
    try:
        after = float(after)
    except:
        return Response('wrong format', 400)

    new_messages = [message for message in db if message['time'] > after]

    return {'messages': new_messages}


app.run(debug=True)
