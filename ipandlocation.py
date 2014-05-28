from flask import Flask
from flask import jsonify
from flask import request
import requests

# this function will return an ip address


def getip():
    #return jsonify({'ip' : request.remote_addr }), 200
    return str(request.remote_addr)

def getlocation(ip):
    print("http://api.hostip.info/get_json.php?ip=%s" % ip)
    r = requests.get("http://api.hostip.info/get_json.php?ip=%s" % ip)
    unencoded = r.text
    data =  unencoded.encode("utf8")
    return data


