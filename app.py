#!/usr/bin/python3
from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"*": {"origins": "0.0.0.0"}})

@app.route("/", strict_slashes=False)
def index():
    """Show index
    """
    return render_template('index.html')

@app.route("/send", methods=['GET'])
def send_mesagge():
    """
    Sends message to Chatbot API
    """
    message  = request.url
    message = message[33:]
    message = str(message).replace('+', ' ')
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run('0.0.0.0', '5000', threaded=True)
