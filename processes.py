# some processes to control with at least one input an one output

import numpy as np
import time
import threading

class Process(threading.Thread):
    def __init__(self,rate_of_change,u,init_value):
        self.rate_of_change = rate_of_change
        self.u = u
        self.init_value  = init_value
        self.measurement = 0
        self.delay = 0
        self.noise = 0
        self.running = False
        self.start_time = 0
    def measure(self):
        return self.measurement
    def feed(self,value):
        self.u = value
    def restart_time(self):
        self.start_time = time.time()
    def stop_process(self):
        self.running = False
    def start_process(self):
        self. restart_time()
        self.running = True
        while(self.running):
            t =time.time()- self.start_time
            self.init_value = self.init_value + self.rate_of_change(t,self.u) # this is the model init + rate of change
            # time.sleep(self.delay)
            self.measurement =  self.init_value + self.noise
            time.sleep(0.2)
            #print(self.measurement)
    def run(self):
        global 

def get_data(object):
    for i in range(100):
        print(object.measure())
        time.sleep(1)

if __name__ == "__main__":
    T = lambda t,u:100*t-t**2-u
    reactor = Process(T,0,25)
    t1 =threading.Thread(target=reactor.start_process())
    t2 = threading,Thread(target=get_data(reactor))
   # t2.start()
   # print("t2 started")
   # t1.start()
   # print("t1 started")
   # t2.start()
   # print("t2 started")
    t2.join()
    reactor.stop_process()
    t1.join()
    #reactor.join()
