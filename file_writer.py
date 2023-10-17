
with open("file2.txt",'a') as file:
	string = input("give string: ")
	file.write(string+',')
