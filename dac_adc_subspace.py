import serial
from matplotlib import pyplot as plt
import numpy as np
import measure_once as mo
import write_command as wc
import time


def dac_set(ser,val):
	str1 = wc.number_to_str5(val)
	wc.write_string(ser,"{D011"+str1+"}")

def adc_read(ser):
	return(mo.measure_once(ser,"{A20000000}"))



if(__name__=='__main__'):
	# test code
	ser = serial.Serial("/dev/ttyAMA0",9600)
	dac_set(ser,1000)
	time.sleep(0.1)
	print(adc_read(ser))
	#works
