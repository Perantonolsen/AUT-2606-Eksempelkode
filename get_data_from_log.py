from matplotlib import pyplot as plt


def eval2(string2):
	return eval(string2[0])*10+eval(string2[1])

data = []
time = []

with open("log.txt",'r') as file:
	for lines in file:
		number = eval(lines.split(' ')[-1])
		lines_split=lines.split(':')
		h = eval2(lines_split[0])
		m = eval2(lines_split[1])
		s = eval2(lines_split[2])
		#print("h: ", h, " m: ", m, " s: ", s, "n: ", number)
		if h == 14:
			data.append(number)
			time.append(s)
plt.plot(time, data)
plt.show()
input()
