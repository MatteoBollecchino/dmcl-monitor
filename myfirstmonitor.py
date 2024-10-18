# My First Monitor
# general goal: read every second the CPU usage

from time import sleep
# or: from time import *
# or: import time 
import psutil

def read_cpu_usage():
    cpu_t = psutil.cpu_times()
    usr_sp_cputime = cpu_t.user
    idle_time = cpu_t.idle
    return usr_sp_cputime, idle_time, cpu_t


# main function
if __name__ == "__main__":
    while True:
        u_t, i_t, cpu_usage = read_cpu_usage()
        # print("user time: " + str(u_t) + ", idle time: " + str(i_t))
        print("user time: %.2f, idel time: %.2f" % (u_t, i_t))
        sleep(1)