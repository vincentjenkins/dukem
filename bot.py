import os
import requests

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'You could put any content here you like, perhaps even a homepage for your bot!'


@app.route('/', methods=['POST'])
def receive():
    data = request.json
    print('Incoming message:')
    print(data['sender_type'])
    print(data['text'])
    print(data['name'])

    # Prevent self-reply
    if data['sender_type'] != 'bot':
        print('not a bot')
        if data['text'].startswith('/ping'):
            send(data['name'] + ' pinged me!')

    return 'ok', 200


def send(msg):
    url  = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': '4e322229309cfb839189723c1d',
        'text': msg,
    }
    r = requests.post(url, data=data)
