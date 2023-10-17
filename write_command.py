#import serial
#import time
#import sys
#import RPi.GPIO as gpio



#ser = serial.Serial("/dev/ttyAMA0",9600) # serial communication opened
#ser = serial.Serial("/dev/ttyS0",9600)

def number_to_str5(number):
	tmp = str(number)
	n = ""
	for i in range(5-len(tmp)):
		 n+="0"
	n+= tmp
	return n
import time
def write_string(ser, string):
	for i in (string):
		ser.write(i.encode('utf-8'))
		time.sleep(0.01)

if __name__ == '__main__':
	import serial
	import time
	import sys
	ser = serial.Serial("/dev/ttyAMA0",9600)
	arguments = sys.argv
	str1 = str(arguments[1])
	print(str1)
	write_string(ser,str1)
	ser.close()
