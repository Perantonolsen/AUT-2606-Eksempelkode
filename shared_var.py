import threading
import time

#mutex = threading.Lock()
shared = 0
lock = False

def plus():
    global shared
    global lock
    while(True):
        if(lock):
            #mutex.acquire()
            shared +=1
            print(shared)
            #mutex.release()
            #time.sleep(0.01)
            lock = False

def minus():
    global shared
    global lock
    while(True):
        if(not lock):
            #mutex.acuire()
            shared-=1
            print(shared)
            #mutex.release()
            #time.sleep(0.01)
            lock = True


if __name__ == "__main__":
    t1 = threading.Thread(target=plus)
    t2 = threading.Thread(target=minus)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
