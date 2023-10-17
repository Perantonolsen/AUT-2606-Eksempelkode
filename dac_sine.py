import serial
import time
import RPi.GPIO as gpio
import numpy as np

buffer = ""
ser = serial.Serial("/dev/ttyAMA0",9600) # serial communication opened
#ser = serial.Serial("/dev/ttyS0",9600)

def number_to_str5(number):
	tmp = str(number)
	n = ""
	for i in range(5-len(tmp)):
		 n+="0"
	n+= tmp
	return n

def write_string(string):
	for i in (string):
		ser.write(i.encode('utf-8'))
		time.sleep(0.01)

if __name__ == '__main__':
	#arguments = sys.argv
	#str1 = str(arguments[1])
	#print(str1)
	#write_string(str1)
	#for i in range(100):
	#	#print(number_to_str5(i))
	#	write_string(("{D011"+number_to_str5(i*10)+"}"))
	#	#print(("{D011"+number_to_str5(i)+"}"))
	#	time.sleep(0.0001)

	for i in range(10000):
		x = np.sin(i/1000)
		write_string(("{B011"+number_to_str5(x*500+500)+"}"))
		time.sleep(0.01)
	ser.close()

