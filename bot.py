import os
import requests
import time

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
    
    #send text
    def sendmsg(msg):
        url = 'https://api.groupme.com/v3/bots/post'
        postData = {
            'bot_id': '4e322229309cfb839189723c1d',
            'text': msg,
        }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=postData, headers=headers)
        print('send url found')
        print(r.status_code)
        print(r.text)
    
    #send image
    def sendimg(img):
        url = 'https://api.groupme.com/v3/bots/post'
        postData = {
            'bot_id': '4e322229309cfb839189723c1d',
            'attachments': [
                {
                    'type': 'image',
                    'url': img,
                }
            ]
        }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=postData, headers=headers)
        print('send url found')
        print(r.status_code)
        print(r.text)
    
    # Prevent self-reply
    if data['sender_type'] != 'bot':
        print('not a bot')
        cleaneddata = data['text'].lower
        if "you're fucked kid" in cleaneddata:
            print('holy shit')
        if data['text'].startswith('/ping'):
            print('sending data')
            sendmsg(data['name'] + ' pinged me!')
        
        elif data['text'].startswith('TYLA'):
            print('sending data')
            sendmsg('TYLA')

        elif data['text'].startswith('image'):
            print('sending data')
            sendimg('https://i.groupme.com/5180x3000.jpeg.ce5c3dac82c7411cab8b162ffcbdfefa')

    return 'ok', 200




'''def sendmsg(msg):
    url  = 'https://api.groupme.com/v3/groups/71853659/messages'
    print('send url found')
    data = {
        'bot_id': '4e322229309cfb839189723c1d',
        'text': data['name'] + ' pinged me!',
    }
    r = requests.post(url, data=data)#'''
