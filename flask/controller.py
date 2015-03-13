import os
import wiringpi

# -------------------------------------------------- #
# define                                             #
# -------------------------------------------------- #
PIN_L1 = 4
PIN_L2 = 17
PIN_R1 = 11
PIN_R2 = 9

class Controller(object):
	def __init__(self, mid):
		self.id = mid
		os.system('gpio export '+ str(PIN_L1) + ' out')
		os.system('gpio export '+ str(PIN_L2) + ' out')
		os.system('gpio export '+ str(PIN_R1) + ' out')
		os.system('gpio export '+ str(PIN_R2) + ' out')
#		self.io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
#		self.io.pinMode(PIN_L1, self.io.OUTPUT)
#		self.io.pinMode(PIN_L2, self.io.OUTPUT)
#		self.io.pinMode(PIN_R1, self.io.OUTPUT)
#		self.io.pinMode(PIN_R2, self.io.OUTPUT)

	def getId(self):
		return self.id

	def motorDrive(self, iIn1Pin, iIn2Pin, rate):
		if rate > 0:
			os.system('gpio -g write ' + str(iIn1Pin) +' 1')
			os.system('gpio -g write ' + str(iIn2Pin) +' 0')
#			self.io.digitalWrite(iIn1Pin, self.io.HIGH)
#			self.io.digitalWrite(iIn2Pin, self.io.LOW)
		elif rate == 0:
			os.system('gpio -g write ' + str(iIn1Pin) +' 0')
			os.system('gpio -g write ' + str(iIn2Pin) +' 0')
#			self.io.digitalWrite(iIn1Pin, self.io.LOW)
#			self.io.digitalWrite(iIn2Pin, self.io.LOW)
		else:
			os.system('gpio -g write ' + str(iIn1Pin) +' 0')
			os.system('gpio -g write ' + str(iIn2Pin) +' 1')
#			self.io.digitalWrite(iIn1Pin, self.io.LOW)
#			self.io.digitalWrite(iIn2Pin, self.io.HIGH)

	# -------------------------------------------------- #
	# motion setting (5 patterns)                        #
	# -------------------------------------------------- #
	def changeMode(self, mode):
		if mode == 'stop':
			self.motorDrive(PIN_L1, PIN_L2, 0)
			self.motorDrive(PIN_R1, PIN_R2, 0)
			return 'changed'
		elif mode == 'forward':
			self.motorDrive(PIN_L1, PIN_L2, 1)
			self.motorDrive(PIN_R1, PIN_R2, 1)
			return 'changed'
		elif mode == 'backward':
			self.motorDrive(PIN_L1, PIN_L2, -1)
			self.motorDrive(PIN_R1, PIN_R2, -1)
			return 'changed'
		elif mode == 'right':
			self.motorDrive(PIN_L1, PIN_L2, 1)
			self.motorDrive(PIN_R1, PIN_R2, -1)
			return 'changed'
		elif mode == 'left':
			self.motorDrive(PIN_L1, PIN_L2, -1)
			self.motorDrive(PIN_R1, PIN_R2, 1)
			return 'changed'
		else:
			return 'error'