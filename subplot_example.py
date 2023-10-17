
#matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt

m = 100
n = 100
#matrix = np.ones(0,1,m*n).reshape(m,n)
t = np.linspace(0,np.pi,100)
X = []
for i in range(100):
	X.append(np.sin(i*t))
fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()

fig.show()
fig.canvas.draw()

for i in range(0,100):
    ax.clear()
    ax.plot(t,X[i])
    fig.canvas.draw()

    
