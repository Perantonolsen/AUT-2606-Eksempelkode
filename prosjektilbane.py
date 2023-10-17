
#matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
steps = 100
t = np.linspace(0,15,steps)
x = np.zeros(steps)
y = np.zeros(steps)
x_d = np.zeros(steps)
y_d = np.zeros(steps)
x_dd = np.zeros(steps)
y_dd = np.zeros(steps)
theta = np.pi/4
g = 9.81
v_canon = 5
y_d[0] =np.sin(theta)*v_canon
x_d[0] =np.cos(theta)*v_canon
y[0] = 1

h= 1/steps
stop = 0
for i in range(steps-1):
    y_dd[i] = -g
    y_d[i+1] = y_d[i] + y_dd[i]*h
    x_d[i+1] = x_d[i] + x_dd[i]*h
    y[i+1] = y[i] + y_d[i]*h
    x[i+1] = x[i] + x_d[i]*h
    if y[i+1] <=0:
        stop = i
        break

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()
fig.show()
fig.canvas.draw()
ax.set_xlim([0,10])
ax.set_ylim([0,10])

for i in range(stop):
    #ax.axis('equal')
    ax.clear()
    #ax.plot(x,y)
    ax.plot(x[i],y[i],'*')
    ax.plot(x[:i],y[:i],'--')
    ax.set_xlim([0,5])
    ax.set_ylim([0,3])
    fig.canvas.draw()
