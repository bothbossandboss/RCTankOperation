#update 2015-3-11
import os
import time
from flask import Flask, jsonify

#import wiringpi
#class : control motor
from controller import Controller

speed = "full"

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!!!!!!"

@app.route("/abc")
def abc():
	return "abcdefg"

@app.route("/ar")
def ar():
	os.system('sudo python /home/pi/flask/pwm_control.py '+str(4)+' '+str(17)+' '+str(0)+' '+str(50))
	#os.system('sudo python /home/pi/flask/pwm_control.py '+str(11)+' '+str(9)+' '+str(0)+' '+str(50))
	return "AR Ohsugi Yasuhito"

@app.route("/sample/<id>", methods=['GET', 'POST'])
def sample(id):
	list = [{"status":"success", "error":"null"},
			{"access":"home", "id":id}]
	return jsonify(results=list)

#control method
#@app.route("/move/<direction>", methods=['GET', 'POST'])
#def move(direction):
#	print speed
#	controller = Controller(speed)
#	result = controller.controlTank(direction)
#	return result
@app.route("/move/stop/<speed>", methods=['GET', 'POST'])
def pwmSrop(speed):
	controller = Controller(speed)
	result = controller.controlTank('stop')
	return result

@app.route("/move/forward/<speed>", methods=['GET', 'POST'])
def pwmForward(speed):
	controller = Controller(speed)
	result = controller.controlTank('forward')
	return result

@app.route("/move/backward/<speed>", methods=['GET', 'POST'])
def pwmBackward(speed):
	controller = Controller(speed)
	result = controller.controlTank('backward')
	return result

@app.route("/move/left/<speed>", methods=['GET', 'POST'])
def pwmLeft(speed):
	controller = Controller(speed)
	result = controller.controlTank('left')
	return result

@app.route("/move/right/<speed>", methods=['GET', 'POST'])
def pwmRight(speed):
	controller = Controller(speed)
	result = controller.controlTank('right')
	return result

if __name__ == "__main__":
    app.run(host='192.168.10.220', port=80, debug=True)