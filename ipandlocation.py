from flask import Flask
from flask import jsonify
from flask import request

# this function will return an ip address


def getip():
    #return jsonify({'ip' : request.remote_addr }), 200
    return request.remote_addr, 200

