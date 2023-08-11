import threading
import time

def function1(seconds):
    print("function sleep for ",seconds)
    time.sleep(seconds)
time1=time.perf_counter()
function1(4)
function1(2)
function1(1)
time2=time.perf_counter()
print("Before threading Time Taken is ",(time2-time1))
time1=time.perf_counter()

t1=threading.Thread(target=function1,args=[4])
t2=threading.Thread(target=function1,args=[1])
t3=threading.Thread(target=function1,args=[1])

t1.start()
t2.start()
t3.start()
time2=time.perf_counter()

print("After threading Time Taken is without wating  for the task to be completed ",(time2-time1))

time1=time.perf_counter()

t1=threading.Thread(target=function1,args=[4])
t2=threading.Thread(target=function1,args=[1])
t3=threading.Thread(target=function1,args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
time2=time.perf_counter()
print("After threading Time Taken is with waiting ",(time2-time1))
