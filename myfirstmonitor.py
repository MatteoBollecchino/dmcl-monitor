# My First Monitor
# general goal: read every second the CPU usage

import csv
from time import sleep
# or: from time import *
# or: import time 
import psutil

# Function for CPU
def read_cpu_usage():
    cpu_t = psutil.cpu_times()
    usr_sp_cputime = cpu_t.user
    idle_time = cpu_t.idle
    cpu_dict = {"user time: ": usr_sp_cputime, " idle time: ": idle_time}
    cpu_dict["interrupt_time"] = cpu_t.interrupt
    return cpu_dict

# Functions for Battery
def time_conversion(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

def read_battery_information():
    battery = psutil.sensors_battery()
    print("Percentuale batteria: ", battery.percent)
    print("Attaccato alla corrente: ", battery.power_plugged)
    print("Tempo rimanente: ", time_conversion(battery.secsleft))

# Function for Memory
def read_memory_usage():
    pass

# Function for Excel File
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

# Main Function
first_time = True
if __name__ == "__main__":
    while True:
        cpu_dict = read_cpu_usage()
        battery_dict = read_battery_information()
        memory_dict = read_memory_usage()
        write_dict_to_csv("my_first_dataset.csv", cpu_dict,first_time)
        write_dict_to_csv("my_first_dataset.csv", battery_dict,first_time)
        write_dict_to_csv("my_first_dataset.csv", memory_dict,first_time)
        first_time = False
        # print("user time: " + str(u_t) + ", idle time: " + str(i_t))
        # print("user time: %.2f, idel time: %.2f" % (u_t, i_t))
        print(cpu_dict)
        print(battery_dict)
        print(memory_dict)
        sleep(1)