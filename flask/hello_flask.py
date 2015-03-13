#update 2015-3-11
import os
import time
from flask import Flask, jsonify

import wiringpi
#class : control motor
from controller import Controller

debugId = "1"

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!!!!!!"

@app.route("/abc")
def abc():
	return "abcdefg"

@app.route("/ar")
def ar():
	os.system('gpio export 24 out')
	os.system('gpio -g write 24 1')
	return "AR Ohsugi Yasuhito"

@app.route("/sample/<id>", methods=['GET', 'POST'])
def sample(id):
	list = [{"status":"success", "error":"null"},
			{"access":"home", "id":id}]
	return jsonify(results=list)

#control method
@app.route("/move/<direction>", methods=['GET', 'POST'])
def move(direction):
	controller = Controller(debugId)
	result = controller.changeMode(direction)
	return result

if __name__ == "__main__":
    app.run(host='192.168.10.220', port=80, debug=True)