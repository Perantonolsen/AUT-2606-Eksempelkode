import serial
from time import sleep
buffer = ""

#ser = serial.Serial("/dev/ttyS0",9600)
ser = serial.Serial("/dev/ttyAMA0",9600)
while True:
	tmp = ser.read().decode('utf-8', errors='ignore')
	if (tmp == '\n'):
		print(buffer)
		buffer = ""
	else:
		buffer += tmp
	sleep(0.03)
