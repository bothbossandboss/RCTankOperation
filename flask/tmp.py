import os
import wiringpi
os.system('gpio export 24 out')

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
io.pinMode(24, io.OUTPUT)
io.digitalWrite(24, io.HIGH)