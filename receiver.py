import requests

response = requests.get('http://127.0.0.1:5000/get_message')

if response.status_code == 200:
    messages = response.json()['messages']

    for messages in messages:
        print(messages)
