import threading
import time

def f():
    print("hei")
    time.sleep(1)

if __name__=="__main__":
    t1 = threading.Thread(target=f)
    t1.start()
    t1.join()

