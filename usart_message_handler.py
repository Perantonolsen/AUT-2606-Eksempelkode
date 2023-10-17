
import serial
import time

buffer = ""
ser = serial.Serial("/dev/ttyS0",9600) # serial communication opened

def write_string(string):
	string = bytes(string,'utf-8')
	for i in string:
		ser.write(i)
		time.sleep(0.01)

if __name__ == '__main__':
	for i in range(10):
		write_string("<message from PI>")
		while True:
			tmp = ser.read().decode('utf-8',errors='ignore')
			if (tmp == '\n'):
				print(buffer)
				buffer = ""
				break
		else:
			buffer += tmp
			time.sleep(0.01)
		time.sleep(1)
	
