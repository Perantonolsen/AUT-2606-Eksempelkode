import serial
import time
import sys
import matplotlib.pyplot as plt

buff = ""
ser = serial.Serial("/dev/ttyAMA0",9600) # serial communication opened
arr = []

def write_string(string):
	#string = bytes(string,'utf-8')
	for i in string:
		ser.write(i.encode('utf-8'))
		#ser.write(i)
		#print(i)
		time.sleep(0.01)
def eval2(str5):
	number = 0
	for i in range(5):
		number += eval(str5[-i])*10**i
	return number

if __name__ == '__main__':
	argument = str(sys.argv[1])
	for i in range(10):
		write_string(argument)
		while True:
			tmp = ser.read().decode('utf-8',errors='ignore')
			if (tmp == '\n'):
				print(buff)
				arr.append(eval2(buff))
				buff = ""
				break
			else:
			    buff += tmp
			    time.sleep(0.01)
		time.sleep(1)
	ser.close()
	plt.plot(arr)
	plt.show()

