#!/usr/bin/python3
from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

@app.route("/send", methods=['GET'])
def send_mesagge():
    """
    Sends message to Chatbot API
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', '5000', threaded=True)