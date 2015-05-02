import subprocess
import signal
import os
import sys
import wiringpi
import time

# -------------------------------------------------- #
# define Raspberry Pi Pins                           #
# -------------------------------------------------- #
#PIN_L1 = 4
#PIN_L2 = 17
#PIN_R1 = 11
#PIN_R2 = 9
PIN_L1 = 26
PIN_L2 = 19
PIN_R1 = 27
PIN_R2 = 17

HALF_SPEED = 5

COMMAND = 'sudo python /home/pi/flask/pwm_control.py '

class Controller(object):
	# -------------------------------------------------- #
	# init class                                         #
	# -------------------------------------------------- #
	def __init__(self, mspeed):
		self.speed = mspeed
		os.system('gpio export '+ str(PIN_L1) + ' out')
		os.system('gpio export '+ str(PIN_L2) + ' out')
		os.system('gpio export '+ str(PIN_R1) + ' out')
		os.system('gpio export '+ str(PIN_R2) + ' out')

	def getSpeed(self):
		return self.speed

	# -------------------------------------------------- #
	# control voltage of pin (HIGH/LOW)                  #
	# -------------------------------------------------- #
	def motorDrive(self, iIn1Pin, iIn2Pin, rate):
		if rate > 0:
			os.system('gpio -g write ' + str(iIn1Pin) +' 1')
			os.system('gpio -g write ' + str(iIn2Pin) +' 0')
		elif rate == 0:
			os.system('gpio -g write ' + str(iIn1Pin) +' 0')
			os.system('gpio -g write ' + str(iIn2Pin) +' 0')
		else:
			os.system('gpio -g write ' + str(iIn1Pin) +' 0')
			os.system('gpio -g write ' + str(iIn2Pin) +' 1')

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

	def pwmMode(self, mode, speed):
		if mode == 'stop':
			self.motorDrive(PIN_L1, PIN_L2, 0)
			self.motorDrive(PIN_R1, PIN_R2, 0)
			return 'changed'
		elif mode == 'forward':
			os.system(str(COMMAND)+' '+str(PIN_L1)+' '+str(PIN_L2)+' '+str(speed)+' '+str(0)+' '+str(PIN_R1)+' '+str(PIN_R2)+' '+str(speed)+' '+str(0))
			self.changeMode('forward')
			return 'changed'
		elif mode == 'backward':
			os.system(str(COMMAND)+' '+str(PIN_L1)+' '+str(PIN_L2)+' '+str(0)+' '+str(speed)+' '+str(PIN_R1)+' '+str(PIN_R2)+' '+str(0)+' '+str(speed))
			self.changeMode('backward')
			return 'changed'
		elif mode == 'right':
			os.system(str(COMMAND)+' '+str(PIN_L1)+' '+str(PIN_L2)+' '+str(speed)+' '+str(0)+' '+str(PIN_R1)+' '+str(PIN_R2)+' '+str(0)+' '+str(speed))
			self.changeMode('right')
			return 'changed'
		elif mode == 'left':
			os.system(str(COMMAND)+' '+str(PIN_L1)+' '+str(PIN_L2)+' '+str(0)+' '+str(speed)+' '+str(PIN_R1)+' '+str(PIN_R2)+' '+str(speed)+' '+str(0))
			self.changeMode('left')
			return 'changed'
		else:
			return 'error'

	def controlTank(self, mode):
		print self.speed
		if self.speed == 'full':
			return self.changeMode(mode)
		elif self.speed == 'half':
			return self.pwmMode(mode, HALF_SPEED)
		return 'error'
