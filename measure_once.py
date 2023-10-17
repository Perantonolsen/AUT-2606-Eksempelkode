import serial
import time
import sys



#ser = serial.Serial("/dev/ttyAMA0",9600)

def str_array2number(str_5):
	number = 0
	number += 10000*eval(str_5[0])
	number += 1000*eval(str_5[1])
	number += 100*eval(str_5[2])
	number += 10*eval(str_5[3])
	number += eval(str_5[4])
	return number

def write_string(ser,string):
	for i in string:
		ser.write(i.encode('utf-8'))
		time.sleep(0.01)

def eval2(str5):
	number = 0
	for i in range(5):
		number += eval(str5[-i])*10**i
	return number


def measure_once(ser,command):
	buff = ""
	write_string(ser,command)
	t0 = time.time()
	while True:
		tmp = ser.read().decode('utf-8',errors='ignore')
		#if(buff == "" and (time.time()-t0) > 0.5):
		#	print("NO_ANSWER")
		#	return "NaN"
		if (tmp == '\n'):
			return str_array2number(buff)
		elif((time.time()-t0) >0.5):
			print("timed out")
			return str_array2number(buff)
		else:
			buff += tmp
		time.sleep(0.01)

if __name__ == "__main__":
	ser = serial.Serial("/dev/ttyAMA0",9600)
	num = measure_once(ser,sys.argv[1])
	print(sys.argv[1], " gave: ",num)
	ser.close()
