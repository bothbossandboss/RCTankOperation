import os
import sys
import wiringpi2

argvs = sys.argv

OUTPUT = 1

PIN_TO_PWM_L1 = int(argvs[1])
PIN_TO_PWM_L2 = int(argvs[2])
PARAM_L1 = int(argvs[3]) #L1 speed
PARAM_L2 = int(argvs[4]) #L2 speed
PIN_TO_PWM_R1 = int(argvs[5])
PIN_TO_PWM_R2 = int(argvs[6])
PARAM_R1 = int(argvs[7]) #R1 speed
PARAM_R2 = int(argvs[8]) #R2 speed

wiringpi2.wiringPiSetupGpio()

wiringpi2.pinMode(PIN_TO_PWM_L1, OUTPUT)
wiringpi2.pinMode(PIN_TO_PWM_L2, OUTPUT)
wiringpi2.pinMode(PIN_TO_PWM_R1, OUTPUT)
wiringpi2.pinMode(PIN_TO_PWM_R2, OUTPUT)

wiringpi2.softPwmCreate(PIN_TO_PWM_L1, 0, 100) # Setup PWM using Pin, Initial Value and Range parameters
wiringpi2.softPwmCreate(PIN_TO_PWM_L2, 0, 100) # Setup PWM using Pin, Initial Value and Range parameters
wiringpi2.softPwmCreate(PIN_TO_PWM_R1, 0, 100) # Setup PWM using Pin, Initial Value and Range parameters
wiringpi2.softPwmCreate(PIN_TO_PWM_R2, 0, 100) # Setup PWM using Pin, Initial Value and Range parameters

count = 0
while 1 :
	wiringpi2.softPwmWrite(PIN_TO_PWM_L1,PARAM_L1) # Change PWM duty cycle
	wiringpi2.delay(10)
	wiringpi2.softPwmWrite(PIN_TO_PWM_L2,PARAM_L2) # Change PWM duty cycle
	wiringpi2.delay(10)
	wiringpi2.softPwmWrite(PIN_TO_PWM_R1,PARAM_R1) # Change PWM duty cycle
	wiringpi2.delay(10)
	wiringpi2.softPwmWrite(PIN_TO_PWM_R2,PARAM_R2) # Change PWM duty cycle
	wiringpi2.delay(10)
	count += 40
	if count > 5000 :
		sys.exit()