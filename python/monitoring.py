#!/usr/bin/env python

import os, platform, subprocess, socket, psutil, netifaces, cpuinfo

#command = "cat /proc/cpuinfo"
#print(subprocess.check_output(command, shell=True).strip())

kb = float(1024)
mb = float(kb ** 2)
gb = float(kb ** 3)

memTotal = int(psutil.virtual_memory()[0]/gb)
memFree = int(psutil.virtual_memory()[1]/gb)
memUsed = int(psutil.virtual_memory()[3]/gb)
memPercent = int(memUsed/memTotal*100)
storageTotal = int(psutil.disk_usage('/')[0]/gb)
storageUsed = int(psutil.disk_usage('/')[1]/gb)
storageFree = int(psutil.disk_usage('/')[2]/gb)
storagePercent = int(storageUsed/storageTotal*100)
info = cpuinfo.get_cpu_info()['brand']

def service():
    print()
    pidTotal = len(psutil.pids())
    print("Running process: ", pidTotal)

def load_avg():
    print()
    print('---------- Load Average ----------')
    print()
    print("Load avg (1 mins)  :",round(os.getloadavg()[0],2))
    print("Load avg (5 mins)  :",round(os.getloadavg()[1],2))
    print("Load avg (15 mins) :",round(os.getloadavg()[2],2))

def system():
    core = os.cpu_count()
    host = socket.gethostname()
    print()
    print('---------- System Info ----------')
    print()
    print("Hostname     :",host)
    print("System       :",platform.system(),platform.machine())
    print("Kernel       :",platform.release())
    print('Compiler     :', platform.python_compiler())
    print('CPU          :',info, core,"(Core)")
    print("Memory       :", memTotal,"GiB")
    print("Disk         :", storageTotal,"GiB")

def cpu():
    print()
    print('---------- CPU ----------')
    print()
    print("CPU Usage    : ",cpuUsage,"GiB")

def memory():
    print()
    print('---------- RAM & Disk usage ----------')
    print()
    print("RAM Used         : ",memUsed,"GiB /",memTotal,"GiB","(",memPercent,"%",")")
    print("Disk Used        : ",storageUsed,"GiB /",storageTotal,"GiB","(",storagePercent,"%",")")

def network():
    active = netifaces.gateways()['default'][netifaces.AF_INET][1]
    speed = psutil.net_io_counters(pernic=False)
    sent = speed[0]
    psend = round(speed[2]/kb, 2)
    precv = round(speed[3]/kb, 2)
    print()
    print('---------- Network stat ----------')
    print()
    print("Active interface : ",active)
    print("Packet send      : ",psend,"KiB/s")
    print("Packet receive   : ",precv,"KiB/s")

def main():
    service()
    system()
    load_avg()
    memory()
    network()

main()