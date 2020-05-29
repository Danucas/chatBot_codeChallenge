#!/usr/bin/python3
import requests
from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"*": {"origins": "0.0.0.0"}})


@app.route("/", strict_slashes=False)
def index():
    """Show index
    """
    return render_template('index.html')


@app.route("/send", methods=['GET', 'POST'])
def send_mesagge():
    """
    Sends message to Chatbot API
    """
    header = {}
    header['authorization'] = 'Bearer pspo4eqrrXfHmdNEM_UKuXGnYVRUGPWY'
    header['content-type'] = 'application/json'

    if request.method == 'POST':
        message = request.form['message']
    data = {
        'query': 'message',
        'sessionId': '92354782222'
    }
    req = requests.post('https://api.chatbot.com/query', headers=header, data=data)
    print(req.content)
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run('0.0.0.0', '5000', threaded=True)
