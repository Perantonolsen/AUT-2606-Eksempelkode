from matplotlib import pyplot as plt
import numpy as np

f = []
t = []

def eval2(string):
	return eval(string[0])*10+eval(string[1])

with open("log.txt",'r') as file:
	for lines in file:
		number = eval(lines.split(' ')[-1])
		line_s = lines.split(':')
		#seconds = eval2(lines.split(':')[2])
		print(eval2(line_s[0]))
		if(eval2(line_s[0])==14):
			seconds = eval2(line_s[2])
			f.append(number)
			t.append(seconds)
plt.plot(t,f);
plt.show()
input()

