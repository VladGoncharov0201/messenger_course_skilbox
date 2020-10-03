import requests

response = requests.post('http://127.0.0.1:5000/send_message',
                        json={'text': 'Hi', 'author': 'Gary'})
print(response.text)
