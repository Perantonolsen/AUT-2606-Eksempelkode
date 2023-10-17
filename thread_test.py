import threading
import time
import sys
import numpy as np

running = True
vol = 0
#mutex = threading.Lock()

def process():
    global running
    global vol
    flow_in = 0.1
    flow_out = 0.01
    steptime = 0.00001 # seconds
    while(running):
        vol = vol + flow_in - np.sqrt(vol)*flow_out
        time.sleep(steptime)



def stop():
    global running
    global vol
    for i in range(eval(sys.argv[1])):
        print(vol)
        time.sleep(1)
    running = False


if __name__=="__main__":
    print(sys.argv)
    t1 = threading.Thread(target=process)
    t2 = threading.Thread(target=stop)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
