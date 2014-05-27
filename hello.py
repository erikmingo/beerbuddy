import os
from flask import Flask
from flask import jsonify
from flask import request
import ipandlocation

app = Flask(__name__)

# Bit to show ip address

@app.route('/getmyip', methods=["GET"])
def get_my_ip():
    return ipandlocation.getip()

@app.route('/')
def hello():
    return "Hello World!"
