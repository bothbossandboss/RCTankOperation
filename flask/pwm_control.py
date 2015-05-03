import os
import sys
from RPIO import PWM

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

PWM.setup()
PWM.init_channel(0)
PWM.init_channel(1)
PWM.init_channel(2)
PWM.init_channel(3)

PWM.add_channel_pulse(0, PIN_TO_PWM_L1, 0, PARAM_L1)
PWM.add_channel_pulse(1, PIN_TO_PWM_L2, 0, PARAM_L2)
PWM.add_channel_pulse(2, PIN_TO_PWM_R1, 0, PARAM_R1)
PWM.add_channel_pulse(3, PIN_TO_PWM_R2, 0, PARAM_R2)
