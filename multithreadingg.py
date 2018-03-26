import thread
import time
def task1(threadName,delay):
    while True:
        print threadName
        time.sleep(delay)
def task2(threadName,delay):
    while True:
        print threadName
        time.sleep(delay)
thread.start_new_thread(task1,("satyam",4))
thread.start_new_thread(task1,("bang",2.5))
