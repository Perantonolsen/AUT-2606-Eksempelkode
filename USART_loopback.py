import serial
from time import sleep
buffer = ""
testString = "top kek!"

ser = serial.Serial("/dev/ttyS0",9600)
for i in range(100):
    ser.write(bytes(testString,'utf-8'))
    tmp = ser.read().decode('utf-8',errors='ignore')
    if tmp == '!':
        print(buffer)
        buffer = ""
    else:
        buffer+= tmp
    sleep(0.03)
