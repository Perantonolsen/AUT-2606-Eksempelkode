
#matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
import serial
import time
import sys

buff = ""

ser = serial.Serial("/dev/ttyAMA0",9600)
plotLen = 1000
fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()
fig.show()
fig.canvas.draw()

ax.set_xlim([0,1000])
#ax.set_ylim([0,1023])
ax.set_ylim([0,5000])
seconds = time.time()
counter = 0
lastNumber = 0
t = []
x =[]
x_filtered=[]
def avg_filter(array,size):
    if (size > len(array)+1):
        return array[-1]
    tmp = 0
    for i in range(size):
        tmp+=array[len(array)-(i+1)]
    return tmp/size

def str_array2number(number,str_5):
    number += 10000*eval(str_5[0])
    number += 1000*eval(str_5[1])
    number += 100*eval(str_5[2])
    number += 10*eval(str_5[3])
    number += eval(str_5[4])
    return number

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

if __name__ == "__main__":
	arguments = sys.argv
	command = str(arguments[1])
	try:
		seconds = eval(arguments[2])
	except:
		seconds = 10
	start = time.time()
	while True:
		write_string(command)
		while True:
			number = 0
			tmp = ser.read().decode('utf-8',errors='ignore')
			if (tmp == '\n'):
				lastNumber = str_array2number(number,buff)
				buff = ""
				t.append(time.time()-seconds)
				x.append(lastNumber)
				x_filtered.append(avg_filter(x,2))
				break # word received
			else:
				buff += tmp
			time.sleep(0.01)
			ax.clear()
			ax.plot(t,x,t,x_filtered)
			fig.canvas.draw()
		if(time.time()-start > seconds):
			break
		#time.sleep(1)
	ser.close()
	input()
