#matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
import os
steps = 1000
t = np.linspace(0,1,steps)
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

x_calc = x[0] + x_d[0]*t+0.5*x_dd*t**2
y_calc = y[0] + y_d[0]*t+0.5*(y_dd-g)*t**2
h= 1/steps
stop = 0
m = 1
C = 0.5
# F_d =- C*q_d[i]**2 -> Sum(F) = ma
for i in range(steps-1):
   # if t[i] <= 0.5:
   #     y_dd[i] = -g -np.sign(y_d[i])*C*y_d[i]**2
   #     x_dd[i] = -np.sign(x_d[i])*C*x_d[i]**2
   # else:
    y_dd[i] = -g -np.sign(y_d[i])*C*y_d[i]**4
    x_dd[i] = -np.sign(x_d[i])*C*x_d[i]**4
    y_d[i+1] = y_d[i] + y_dd[i]*h
    x_d[i+1] = x_d[i] + x_dd[i]*h
    y[i+1] = y[i] + y_d[i]*h
    x[i+1] = x[i] + x_d[i]*h
    if y[i+1] <=0:
        stop = i
        break
plt.plot(x[:stop],y[:stop],'--b')
plt.plot(x_calc[:stop],y_calc[:stop],'-r')
plt.show()
#plt.legend= ["numerisk","analytisk"]
input()
#os.system("pause")

