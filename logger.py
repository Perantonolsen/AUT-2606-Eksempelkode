import measure_once as mo
import datetime as dt
import serial
import sys
import os

ser = serial.Serial("/dev/ttyAMA0",9600)

command = sys.argv[1]
answer = mo.measure_once(ser,command)
print(command, " : ", answer)

date = dt.datetime.today().strftime('%Y_%m_%d')
filename = "log"+date+".txt"
if os.path.exists(filename):
	with open(filename,'a+') as file:
		file.write(dt.datetime.today().strftime('%H:%M:%S')+" : "+str(answer)+"\n")
else:
	with open(filename,'w') as file:
                file.write(dt.datetime.today().strftime('%H:%M:%S')+" : "+str(answer)+"\n")

