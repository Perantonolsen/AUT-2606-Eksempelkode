import time
import threading
from matplotlib import pyplot as plt
import numpy as np
import sys

y = 0
u = 0 # theta (mellom -pi/2 -> pi/2)
ref = 0
running = True
sleep_time = 0.0001 #sec

D = 10
x_0 = 2
C_d = 0.1
m = 2
k = 100
g = 9.81
f = lambda v: np.sqrt(v)
T = []
X = []
U = []



def spring_damper_system():
    global u
    global y
    global running
    # start_time = time.time()
    u = 0
    x = 0
    x_d = 5
    x_dd = 0
    x_n = 0
    x_d_n = 0
    while(running):
        #t_1 = time.time()-start_time
        time.sleep(sleep_time)
        #dt = abs(time.time()-t_1 -start_time)
        dt = sleep_time
        x_dd = 1/m*(-k*x - C_d*f(abs(x_d))*np.sign(x_d))-g-u 
        x_d_n = x_d + x_dd*dt
        x_n = x + x_d*dt
        y = D - (x_0+x)
        x = x_n
        x_d = x_d_n
#        print(x, u)

ref =eval(sys.argv[1])
Kp = eval(sys.argv[2])
Ti = eval(sys.argv[3])
Td = eval(sys.argv[4])
#Kp = 0.5 #Kp stående svingninger
#Kp = 0.25
#Ti = 100
#Td = 0.005
Ki = Kp/Ti
Kd = Kp*Td
#ref = -2

def PID_controller():
    global u
    global y
    global running
    e_old = 0
    e_sum  = 0
    e_dot = 0
    h = sleep_time
    while(running):
        e = ref - y
        #if ((e_old-e)/h < 1000):
        #    e_dot = (e_old-e)/h
        e_dot = (e_old-e)/h
        e_old = e
        e_sum += e*h
        #print(e_dot, e_sum)
        u = Kp*e + Kd*e_dot + Ki*e_sum
        time.sleep(h)
    
def stop():
    global running
    for i in range(eval(sys.argv[5])):
        print(i)
        time.sleep(1)
    running = False
    return 0

def plotter_1():
    global running
    global u
    global y
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.ion()
    fig.show()
    fig.canvas.draw()
    ax.set_xlim([0,100])
    ax.set_ylim([-10,10])
    seconds = time.time()
    T = []
    X = []
    U = []
    while running:
        T.append(time.time()-seconds)
        X.append(y)
        U.append(u)
       # time.sleep(0.01)
        ax.clear()
        ax.plot(T,X,T,U,'r--')
        fig.canvas.draw()
        #time.sleep(1)

def assemble():
    global running
    global u
    global y
    global T
    global X
    global U
    seconds = time.time()
    while running:
        T.append(time.time() - seconds)
        #if abs(y) <1000:
        #   X.append(y)
        #else:
        #   X.append(X[-1])
        #if abs(u)<1000:
        #   U.append(u)
        #else:
        #   U.append(U[-1])
        X.append(y)
        U.append(u)
        time.sleep(sleep_time)
if __name__ == "__main__":
    #spring_damper_system()
    #simtime = 10# sec
    
    #refArray = np.zeros(1000)
    t1 = threading.Thread(target=spring_damper_system)
    t2 = threading.Thread(target=PID_controller)
    t3 = threading.Thread(target=stop)
    t4 = threading.Thread(target=plotter_1)
    t4 = threading.Thread(target=assemble)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    #for i in range(len(refArray)):
    #    ref 
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    # plt.plot(T,X,T,U,'r-')
    plt.plot(T,X)
    plt.figure()
    plt.plot(T,U,'r')
    plt.show()
    input()
