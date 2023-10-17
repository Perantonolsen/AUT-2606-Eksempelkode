import threading
import time


def spam():
    for i in range(10):
        print("spam")
        time.sleep(0.3)

def spam2():
    while(True):
        print("spam2")
        time.sleep(0.5)




if __name__ == '__main__':
    t1 = threading.Thread(target=spam)
    t2 = threading.Thread(target=spam2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
   # t2 = threading.Thread(target=spam2)
   # t2.start()
   # t2.join()
