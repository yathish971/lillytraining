from threading import *
import time
import os
from multiprocessing import *
import concurrent.futures
def square(num):
    time.sleep(1)
    print(f"The Process id :{os.getpid()} Thread id :{get_native_id()}")
    print("square of the number is ",num**2)

numbers=[10,20,30,40,50]
if __name__=="__main__":
    print("**********************multi Threading**********************************")
    start_time=time.perf_counter()
    for num in numbers:
        t=Thread(target=square,args=[num])
        t.start()
    t.join()

    end_time=time.perf_counter()
    time.sleep(1)
    print("The total time ",end_time-start_time)
    print("**********************multi process**********************************")
    start_time=time.perf_counter()
    for num in numbers:
        p=Process(target=square,args=[num])
        p.start()
    p.join()

    end_time=time.perf_counter()
    time.sleep(1)
    print("The total time ",end_time-start_time)


    print("**********************thread poll process**********************************")
    start_time=time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(numbers)) as executor:
        
        for num in numbers:
            executor.submit(square,num)

    end_time=time.perf_counter()
    time.sleep(1)
    print("The total time ",end_time-start_time)

    print("**********************process poll process**********************************")
    start_time=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=len(numbers)) as executor:
        
        for num in numbers:
            executor.submit(square,num)

    end_time=time.perf_counter()
    time.sleep(1)
    print("The total time ",end_time-start_time)
