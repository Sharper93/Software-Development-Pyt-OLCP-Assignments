from os import getpid
import multiprocessing as mp
import random
from datetime import datetime
from time import sleep

# 15.1 Mulitprocessing - 3 processes - random wait times betwwen - print time
def mp_process(process_num):
    print("Process ID:", getpid(), ". Process number:", process_num)
    

if __name__ == '__main__':  
# create three processes & iterate for each process
    for i in range(3):
            
        # random number of seconds for processes
        num_seconds = random.random()
        print(num_seconds)
        # pause app
        sleep(num_seconds)
        call_prc = mp.Process(target=mp_process, args=(i,))
        #start process
        call_prc.start()
        # join process
        call_prc.join()
        # print time with random delay
        print(datetime.now())