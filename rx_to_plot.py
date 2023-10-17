
#matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
import serial
import time

buffer = ""
#ser = serial.Serial("/dev/ttyS0",9600) # serial communication opened
ser = serial.Serial("/dev/ttyAMA0",9600)
plotLen = 1000
#matrix = np.ones(0,1,m*n).reshape(m,n)
#t = np.zeros(plotLen)
#x = np.zeros(plotLen)
fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()
fig.show()
fig.canvas.draw()
#ax.set(xlim=(0,1000),ylim=(0,1024))
#0, 1000,0,1024 = ax('image')
#ax.axis([0,1000,0,1024],'image')
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

while True:
    while True:
        number = 0
        tmp = ser.read().decode('utf-8',errors='ignore')
        if (tmp == '\n'):
            #lastNumber = eval(buffer)
            #lastNumber = eval(buffer[3])*10+eval(buffer[4])
            lastNumber = str_array2number(number,buffer)
            buffer = ""
            t.append(time.time()-seconds)
            x.append(lastNumber)
            x_filtered.append(avg_filter(x,7))
            break
        else:
            buffer += tmp
        time.sleep(0.01)
    ax.clear()
    ax.plot(t,x,t,x_filtered)
    fig.canvas.draw()
    #time.sleep(1)
