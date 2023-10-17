import serial
import time
import sys
import RPi.GPIO as gpio


buffer = ""
ser = serial.Serial("/dev/ttyAMA0",9600) # serial communication opened
#ser = serial.Serial("/dev/ttyS0",9600)

def write_string(string):
	for i in (string):
		ser.write(i.encode('utf-8'))
		time.sleep(0.01)

arguments = sys.argv
str1 = str(arguments[1])
print(str1)
write_string(str1)
ser.close()
