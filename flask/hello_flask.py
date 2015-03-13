#update 2015-3-10
import os
import time
from flask import Flask, jsonify

import wiringpi
#class : control motor
from controller import Controller

#PIN_L1 = 4
debugId = "1"

app = Flask(__name__)

# set up
#io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
#io.pinMode(PIN_L1, io.PWM_OUTPUT)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(22, GPIO.OUT)

@app.route("/")
def hello():
#	io.pwmWrite(PIN_L1, 50)
	return "Hello World!!!!!!"

@app.route("/abc")
def abc():
	return "abcdefg"

@app.route("/ar")
def ar():
	os.system('gpio export 24 out')
	os.system('gpio -g write 24 1')
#	gpio = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
#	gpio.pinMode(24, gpio.OUTPUT)
#	gpio.digitalWrite(24, gpio.HIGH)
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
	#app = create_app()
    app.run(host='192.168.10.220', port=80, debug=True)