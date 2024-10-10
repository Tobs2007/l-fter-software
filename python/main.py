#rot=255
#grün=96
#blau=160

import serial
import time
import colorsys
import os
import psutil
from termcolor import colored
import statistics

arduino = serial.Serial(port='COM5', baudrate=500000)
cpu_time=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
global startfps
startfps=time.time()
def setled(fan,index,R,G,B,delay=0.002):
    start=time.time()
    arduino.write(bytes(str(fan) + " " + str(index) + " " + str(R) + " " + str(G) + " " + str(B),   'utf-8'))
    # print(str(fan) + " " + str(index) + " " + str(R) + " " + str(G) + " " + str(B))
    # print(arduino.out_waiting)
    # print(delay)
    elapsed=time.time()-start
    time.sleep(max(delay-elapsed,0))
    if delay<elapsed:
        print(colored(str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5]),"yellow") + colored("     hanging behind delay: " + str(delay) + "   elapsed " + str(elapsed),"red"))
def setledupdate(fan,index,R,G,B,delay=0.001):
    setled(fan,index,R,G,B,delay)
    show()

def show():
    setled(4,0,0,0,0)

def test_patern():
    setled(0,0,255,0,0)
    setled(0,1,255,0,0)
    setled(0,2,255,0,0)
    setled(0,3,255,0,0)
    setled(0,4,255,0,0)
    setled(0,5,255,0,0)
    setled(0,6,255,0,0)
    setled(0,7,255,0,0)
    setled(0,8,255,0,0)

    setled(1,0,0,255,0)
    setled(1,1,0,255,0)
    setled(1,2,0,255,0)
    setled(1,3,0,255,0)
    setled(1,4,0,255,0)
    setled(1,5,0,255,0)
    setled(1,6,0,255,0)
    setled(1,7,0,255,0)
    setled(1,8,0,255,0)
    
    
    setled(2,0,0,0,255)
    setled(2,1,0,0,255)
    setled(2,2,0,0,255)
    setled(2,3,0,0,255)
    setled(2,4,0,0,255)
    setled(2,5,0,0,255)
    setled(2,6,0,0,255)
    setled(2,7,0,0,255)
    setled(2,8,0,0,255)


    setled(3,0,255,0,255)
    setled(3,1,255,255,255)
    setled(3,2,255,0,255)
    setled(3,3,255,255,255)
    setled(3,4,255,0,255)
    setled(3,5,255,255,255)
    show()

def black():
    setled(0,0,0,0,0)
    setled(0,1,0,0,0)
    setled(0,2,0,0,0)
    setled(0,3,0,0,0)
    setled(0,4,0,0,0)
    setled(0,5,0,0,0)
    setled(0,6,0,0,0)
    setled(0,7,0,0,0)
    setled(0,8,0,0,0)

    
    setled(1,0,0,0,0)
    setled(1,1,0,0,0)
    setled(1,2,0,0,0)
    setled(1,3,0,0,0)
    setled(1,4,0,0,0)
    setled(1,5,0,0,0)
    setled(1,6,0,0,0)
    setled(1,7,0,0,0)
    setled(1,8,0,0,0)

    
    setled(2,0,0,0,0)
    setled(2,1,0,0,0)
    setled(2,2,0,0,0)
    setled(2,3,0,0,0)
    setled(2,4,0,0,0)
    setled(2,5,0,0,0)
    setled(2,6,0,0,0)
    setled(2,7,0,0,0)
    setled(2,8,0,0,0)
    
    
    setled(3,0,0,0,0)
    setled(3,1,0,0,0)
    setled(3,2,0,0,0)
    setled(3,3,0,0,0)
    setled(3,4,0,0,0)
    setled(3,5,0,0,0)
    
    show()

def animshowdelay(fan,index,R,G,B,delay):
    setledupdate(fan,index,R,G,B)
    time.sleep(delay)

def anim_RGB():
    black()
    setFans(0,255,0,0,0.2)
    setFans(1,0,255,0,0.2)
    setFans(2,0,0,255,0.2)
    setFans(3,255,0,0,0.2)
    setFans(4,0,255,0,0.2)
    setFans(5,0,0,255,0.2)
    setFans(6,255,0,0,0.2)
    setFans(7,0,255,0,0.2)
    setFans(8,0,0,255,0.2)
    
    setFans(0,0,0,0,0.2)
    setFans(1,0,0,0,0.2)
    setFans(2,0,0,0,0.2)
    setFans(3,0,0,0,0.2)
    setFans(4,0,0,0,0.2)
    setFans(5,0,0,0,0.2)
    setFans(6,0,0,0,0.2)
    setFans(7,0,0,0,0.2)
    setFans(8,0,0,0,0.2)

def anim_custom(R,G,B,speed=0.2):
    black()
    setFans(0,R,G,B,speed)
    setFans(1,R,G,B,speed)
    setFans(2,R,G,B,speed)
    setFans(3,R,G,B,speed)
    setFans(4,R,G,B,speed)
    setFans(5,R,G,B,speed)
    setFans(6,R,G,B,speed)
    setFans(7,R,G,B,speed)
    setFans(8,R,G,B,speed)
    
    setFans(0,0,0,0,speed)
    setFans(1,0,0,0,speed)
    setFans(2,0,0,0,speed)
    setFans(3,0,0,0,speed)
    setFans(4,0,0,0,speed)
    setFans(5,0,0,0,speed)
    setFans(6,0,0,0,speed)
    setFans(7,0,0,0,speed)
    setFans(8,0,0,0,speed)

def anim1(R,G,B,speed=0.2):
    setFans(0,R,G,B,speed)
    setFansNoShow(0,0,0,0)
    setFans(1,R,G,B,speed)
    setFansNoShow(1,0,0,0)
    setFans(2,R,G,B,speed)
    setFansNoShow(2,0,0,0)
    setFans(3,R,G,B,speed)
    setFansNoShow(3,0,0,0)
    setFans(4,R,G,B,speed)
    setFansNoShow(4,0,0,0)
    setFans(5,R,G,B,speed)
    setFansNoShow(5,0,0,0)
    setFans(6,R,G,B,speed)
    setFansNoShow(6,0,0,0)
    setFans(7,R,G,B,speed)
    setFansNoShow(7,0,0,0)
    setFans(8,R,G,B,speed)
    setFansNoShow(8,0,0,0)

def setFans(index,R,G,B,delay):
    setled(0,index,R,G,B)
    setled(1,index,R,G,B)
    setled(2,index,R,G,B)
    show()
    time.sleep(delay)

def setFansNoShow(index,R,G,B):
    setled(0,index,R,G,B)
    setled(1,index,R,G,B)
    setled(2,index,R,G,B)

def hueshift(speed):
    hue = 0
    for hue in range(int(255/speed)):
        hue=hue+speed
        # print(hue)
        # print(colorsys.hsv_to_rgb((hue)/100,1,1))
        index = 0
        for index in range(8):
            colorRaw = colorsys.hsv_to_rgb((hue+index)/255,1,1)
            color = list(colorRaw)
            setFansNoShow(index,int(color[0])*255,int(color[1])*255,int(color[2])*255)
            index=index+1
            # print(index)
    show()
    print(hue)
    time.sleep(0.005)

def system_info(R,G,B,speed=0):



    cpu_usage = psutil.cpu_percent()
    cpu_time.append(int(cpu_usage))
    cpu_time.pop(0)
    cpu_usage = statistics.mean(cpu_time)



    ram_usage = psutil.virtual_memory()[2]
    if True:
        if ram_usage >= 30:
            setled(2,5,R,G,B)
        else:
            setled(2,5,0,0,0)

       
        if ram_usage >= 37:
            setled(2,4,R,G,B)
            setled(2,6,R,G,B)
        else:
            setled(2,4,0,0,0)
            setled(2,6,0,0,0)

            
        if ram_usage >= 44:
            setled(2,3,R,G,B)
            setled(2,7,R,G,B)
        else:
            setled(2,3,0,0,0)
            setled(2,7,0,0,0)

            
        if ram_usage >= 51:
            setled(2,2,R,G,B)
            setled(2,8,R,G,B)
        else:
            setled(2,2,0,0,0)
            setled(2,8,0,0,0)

            
        if ram_usage >= 58:
            setled(2,1,R,G,B)
            setled(2,0,R,G,B)
        else:
            setled(2,1,0,0,0)
            setled(2,0,0,0,0)

            
        if ram_usage >= 65:
            setled(1,5,R,G,B)
        else:
            setled(1,5,0,0,0)

            
        if ram_usage >= 72:
            setled(1,4,R,G,B)
            setled(1,6,R,G,B)
        else:
            setled(1,4,0,0,0)
            setled(1,6,0,0,0)

            
        if ram_usage >= 79:
            setled(1,3,R,G,B)
            setled(1,7,R,G,B)
        else:
            setled(1,3,0,0,0)
            setled(1,7,0,0,0)

            
        if ram_usage >= 86:
            setled(1,2,R,G,B)
            setled(1,8,R,G,B)
        else:
            setled(1,2,0,0,0)
            setled(1,8,0,0,0)

            
        if ram_usage >= 93:
            setled(1,1,R,G,B)
            setled(1,0,R,G,B)
        else:
            setled(1,1,0,0,0)
            setled(1,0,0,0,0)
    
    if True:
        if cpu_usage >= 0:
            setled(0,5,R,G,B)
        else:
            setled(0,5,0,0,0)

            
        if cpu_usage >= 20:
            setled(0,4,R,G,B)
        else:
            setled(0,4,0,0,0)

            
        if cpu_usage >= 30:
            setled(0,3,R,G,B)
        else:
            setled(0,3,0,0,0)

            
        if cpu_usage >= 40:
            setled(0,2,R,G,B)
        else:
            setled(0,2,0,0,0)

            
        if cpu_usage >= 50:
            setled(0,1,R,G,B)
        else:
            setled(0,1,0,0,0)

            
        if cpu_usage >= 60:
            setled(0,0,R,G,B)
        else:
            setled(0,0,0,0,0)

            
        if cpu_usage >= 70:
            setled(0,8,R,G,B)
        else:
            setled(0,8,0,0,0)

            
        if cpu_usage >= 80:
            setled(0,7,R,G,B)
        else:
            setled(0,7,0,0,0)

            
        if cpu_usage >= 90:
            setled(0,6,R,G,B)
        else:
            setled(0,6,0,0,0)
    
    # print("cpu: ", cpu_usage, "   Ram: ",ram_usage, "   list: ",cpu_time)
    show()
    time.sleep(speed)
def meter(speed=0.1):
    black()
    setledupdate(2,5,255,255,255,speed)
    setled(2,4,255,255,255)
    setledupdate(2,6,255,255,255,speed)
    setled(2,3,255,255,255)
    setledupdate(2,7,255,255,255,speed)
    setled(2,2,255,255,255)
    setledupdate(2,8,255,255,255,speed)
    setled(2,1,255,255,255)
    setledupdate(2,0,255,255,255,speed)


    setledupdate(1,5,255,255,255,speed)
    setled(1,4,255,255,255)
    setledupdate(1,6,255,255,255,speed)
    setled(1,3,255,255,255)
    setledupdate(1,7,255,255,255,speed)
    setled(1,2,255,255,255)
    setledupdate(1,8,255,255,255,speed)
    setled(1,1,255,255,255)
    setledupdate(1,0,255,255,255,speed)

    setledupdate(3,0,255,255,255,speed)
    setledupdate(3,1,255,255,255,speed)
    setledupdate(3,2,255,255,255,speed)
    setledupdate(3,3,255,255,255,speed)
    setledupdate(3,4,255,255,255,speed)
    setledupdate(3,5,255,255,255,speed)

    setledupdate(0,5,255,255,255,speed)
    setled(0,4,255,255,255)
    setledupdate(0,6,255,255,255,speed)
    setled(0,3,255,255,255)
    setledupdate(0,7,255,255,255,speed)
    setled(0,2,255,255,255)
    setledupdate(0,8,255,255,255,speed)
    setled(0,1,255,255,255)
    setledupdate(0,0,255,255,255,speed)


    setledupdate(0,0,0,0,0,speed)
    setled(0,1,0,0,0)
    setledupdate(0,8,0,0,0,speed)
    setled(0,2,0,0,0)
    setledupdate(0,7,0,0,0,speed)
    setled(0,3,0,0,0)
    setledupdate(0,6,0,0,0,speed)
    setled(0,4,0,0,0)
    setledupdate(0,5,0,0,0,speed)
    
    setledupdate(3,5,0,0,0,speed)
    setledupdate(3,4,0,0,0,speed)
    setledupdate(3,3,0,0,0,speed)
    setledupdate(3,2,0,0,0,speed)
    setledupdate(3,1,0,0,0,speed)
    setledupdate(3,0,0,0,0,speed)

    setledupdate(1,0,0,0,0,speed)
    setled(1,1,0,0,0)
    setledupdate(1,8,0,0,0,speed)
    setled(1,2,0,0,0)
    setledupdate(1,7,0,0,0,speed)
    setled(1,3,0,0,0)
    setledupdate(1,6,0,0,0,speed)
    setled(1,4,0,0,0)
    setledupdate(1,5,0,0,0,speed)
    
    setledupdate(2,0,0,0,0,speed)
    setled(2,1,0,0,0)
    setledupdate(2,8,0,0,0,speed)
    setled(2,2,0,0,0)
    setledupdate(2,7,0,0,0,speed)
    setled(2,3,0,0,0)
    setledupdate(2,6,0,0,0,speed)
    setled(2,4,0,0,0)
    setledupdate(2,5,0,0,0,speed)

    time.sleep(speed)
def fps_limit(fps=20):
    endfps=time.time()
    global startfps
    frametime=(1/fps)-(endfps-startfps)
    time.sleep(max(0,frametime))
    if frametime<0:
        print("can`t keep up to framerate")
    startfps=time.time()



# test_patern()
time.sleep(1)
while (True):
    system_info(255,48,59,0.02)
    fps_limit(5)
    # anim1(255,0,0)