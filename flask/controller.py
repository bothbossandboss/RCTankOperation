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

FULL_SPEED = 10
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
			return self.pwmMode(mode, FULL_SPEED)
		elif self.speed == 'half':
			return self.pwmMode(mode, HALF_SPEED)
		return 'error'
