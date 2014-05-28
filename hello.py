import os
from flask import Flask
from flask import jsonify
from flask import request
import ipandlocation
import requests

app = Flask(__name__)

# Bit to show ip address

@app.route('/getmyip', methods=["GET"])
def get_my_ip():
    return ipandlocation.getlocation(ipandlocation.getip()), 200
    #return ipandlocation.getlocation(ipandlocation.getip())


@app.route('/')
def hello():
    return requests.get('http://wtfismyip.com/json').text.encode("utf8"), 200


