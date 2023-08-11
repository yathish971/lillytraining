from threading import *

import time

 

def square(num):

    time.sleep(1)

    print("Child Thread: ",num**2)

   

   

numbers=[1,2,3,4,5]

 

start_time=time.time()

 

for num in numbers:

    t=Thread(target=square,args=(num,))

    t.start()

t.join()

 

end_time=time.time()

 

time.sleep(1)

print("The total time: ",end_time-start_time)