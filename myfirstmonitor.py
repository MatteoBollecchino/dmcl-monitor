# My First Monitor
# general goal: read every second the CPU usage

import csv
from time import sleep
# or: from time import *
# or: import time 
import psutil

def read_cpu_usage():
    cpu_t = psutil.cpu_times()
    usr_sp_cputime = cpu_t.user
    idle_time = cpu_t.idle
    cpu_dict = {"user time: ": usr_sp_cputime, " idle time: ": idle_time}
    cpu_dict["interrupt_time"] = cpu_t.interrupt
    return cpu_dict

def write_dict_to_csv(filename, dict_file, first_time):
    if first_time:
        f = open(filename,  'w', newline="") 
    else:
        f = open(filename,  'a', newline="")
        
    w = csv.DictWriter(f,dict_file.keys())

    if first_time:
        w.writeheader()

    w.writerow(dict_file)
    f.close()

# main function
first_time = True
if __name__ == "__main__":
    while True:
        cpu_dict = read_cpu_usage()
        write_dict_to_csv("my_first_dataset.csv", cpu_dict,first_time)
        first_time = False
        # print("user time: " + str(u_t) + ", idle time: " + str(i_t))
        # print("user time: %.2f, idel time: %.2f" % (u_t, i_t))
        print(cpu_dict)
        sleep(1)