import serial
import time

ser = serial.Serial("/dev/ttyS0",9600) # serial communication opened
if __name__ == '__main__':
	while True:
		tmp = ser.read().decode('utf-8',errors='ignore')
		print(tmp)
		time.sleep(1)
