import serial
from time import sleep

buffer = ""

#ser = serial.Serial("/dev/ttyS0",9600)
ser = serial.Serial("/dev/ttyAMA0",9600)
for i in range(10):
    ser.write(input("give: \n").encode('utf-8'))
    buffer += ser.read().decode('utf-8',errors='ignore')
    print(buffer)
    sleep(1)
ser.close()
