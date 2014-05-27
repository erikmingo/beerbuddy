import os
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

# Bit to show ip address

@app.route('/get_my_ip', methods=["GET"])
def get_my_ip():
    return jsonify({'ip' : request.remote_addr}), 200

@app.route('/')
def hello():
    return "Hello World!"
