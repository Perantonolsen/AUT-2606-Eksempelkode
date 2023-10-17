
import numpy as np
import matplotlib.pyplot as plt
import serial
import time

def str_array2number(number,str_5):
    number += 10000*eval(str_5[0])
    number += 1000*eval(str_5[1])
    number += 100*eval(str_5[2])
    number += 10*eval(str_5[3])
    number += eval(str_5[4])
    return number



if __name__ == "__main__":
	ser = serial.Serial("/dev/ttyAMA0",9600)
	#for i in range(10):
	number = 0
	list1 = []
	buf = ""
	c = 0
	while(True):
		tmp = ser.read().decode('utf-8',errors='ignore')	
		if (tmp == '\n'):
			list1.append(str_array2number(number,buf))
			#print(str_array2number(number,buf))
			buf = ""
		else:
			buf+= tmp
		time.sleep(0.1)
		c += 1
		if(c > 100):
			break
	#print(list1)
	plt.plot(range(len(list1)),list1)
	plt.show(block =True)
