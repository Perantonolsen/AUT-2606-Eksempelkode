import numpy as np
import time
import threading

y = 0
u = 0

def run_model(function,iVal):
    start_time = time.time()
    global y
    global u
    iVal_0 = iVal
    #for i in range(100):
    while(True):
        t = time.time() - start_time
        if iVal >= iVal_0:
             iVal = iVal + function(t,u)
        y = iVal
        time.sleep(0.1)

def water_tank():
    #water leaves the tank with constant volume flow of 0.2l/s
    start_time = time.time()
    global y
    global u
    passive_loss = 0.2
    tank_volume = 30    # liters
    #delay = 0.25        # seconds
    vol = 0
    dt = 0.01
    while(True):
        t = time.time() - start_time
        if u < 0: #water can only be added by the pumps
            u = 0
        if u > 5:
            u = 5
        if tank_volume> vol and vol+u  >= dt*passive_loss:
            vol = vol + u -dt*passive_loss
        elif vol > tank_volume:
            vol = 30- dt*passive_loss*vol #spilling water proportional to volume in tank
        else:
            vol = 0
        time.sleep(dt)
        y = vol

def chemical_reactor():
    start_time = time.time()
    global y
    global u
    Temp_coeff = 0.1
    T = 25
    dt = 0.5
    fuel = 1
    u = 0
    while(True):
        if u < 0:
            u = -sqrt(abs(u))
        if fuel + u -T**2 <= 0:
            fuel = u
        else:
            fuel = fuel + u - T**2
        if T+u**2+fuel*T-T*Temp_coeff < 25:
            T = 25
        else:
            T =T+u**2 +fuel*T-T*Temp_coeff
        if T > 1000:
            print(f'T = {T:.3f} Pang!' )
            break
        time.sleep(dt)
        y = T

def PID_controller():
    global u
    ref = 29
    Kp = 0.1
    Ki = 0.05
    Kd = 0.01
    e_old = (ref-y)
    ei = 0
    while(True):
        e = (ref-y)
        ei += (ref-y)
        ed = (e-e_old)/0.3
        u = Kp*e + Ki*ei + Kd*ed
        print(y,u)
        time.sleep(0.3)
        e_old = e




if __name__ == "__main__":
    T = lambda a,b: 10*a -a**2 -b
    # t1 = threading.Thread(target = run_model,args=[T,10],daemon = True)
    # t1 = threading.Thread(target = water_tank,daemon = True)
    t1 = threading.Thread(target = water_tank,daemon = True)
    t2 = threading.Thread(target = PID_controller, daemon = True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
