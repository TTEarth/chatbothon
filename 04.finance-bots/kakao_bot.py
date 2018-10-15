# -*- coding: utf-8 -*- 

from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from urllib.request import urlopen
import json


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
    
@app.route("/keyboard")
def keyboard():
    return jsonify(type="text")

@app.route("/message", methods=["POST"])
def message():
    data = json.loads(request.data)
    content = data["content"]

    if content == str("가상화폐"): # .decode('utf-8') 삭제
        response = urlopen("https://api.bithumb.com/public/ticker/").read().decode('utf8')
        responsejson = json.loads(response)
        coin = responsejson['data']['opening_price']
        content = coin

    response = {
        "message": {
            "text": content
        }
    }

    response = json.dumps(response, ensure_ascii=False)
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80)
    # app.run(host="localhost", port=80)
    # flask 예시 : app.run(host="0.0.0.0", port=5000)