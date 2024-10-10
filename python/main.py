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
import PySimpleGUI as sg
import threading
import keyboard
layout = [  [sg.Text('Choose theme')],
            [sg.Button('System info'), sg.Button('test_pattern'), sg.Button('exit')],
             [sg.Button('anim1'), sg.Button('anim2'),sg.Button('close')] ,
             [sg.Text("Global color")],
             [sg.Text("R"),sg.InputText(default_text='255',enable_events=True,key='R',size=(5,1))],
             [sg.Text("G"),sg.InputText(default_text='30',enable_events=True,key='G',size=(5,1))],
             [sg.Text("B"),sg.InputText(default_text='0',enable_events=True,key='B',size=(5,1))]]
global state
state=1
global fps
fps = 200

global gR
global gG
global gB
gR=255
gG=30
gB=0
arduino = serial.Serial(port='COM5', baudrate=500000)
cpu_time=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
global startfps
startfps=time.time()
def setled(fan,index,R,G,B,delay=0.002):
    start=time.time()
    arduino.write(bytes(str(fan) + " " + str(index) + " " + str(R) + " " + str(G) + " " + str(B),   'utf-8'))
    # print(str(fan) + " " + str(index) + " " + str(R) + " " + str(G) + " " + str(B))
    # print(arduino.out_waiting)
    # print(delay)
    elapsed=time.time()-start
    time.sleep(max(delay-elapsed,0.002))
    if delay<elapsed:
        print(colored(str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5]),"yellow") + colored("     hanging behind delay: " + str(delay) + "   elapsed " + str(elapsed),"red"))
def setledupdate(fan,index,R,G,B,delay=0.001):#sets one led and updates it 
    setled(fan,index,R,G,B,delay)
    show()

def show():#shows the current configuration and calls the fps function
    global fps
    setled(4,0,0,0,0)
    fps_limit(fps)

def scale(val, src, dst):#scales one range to another
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]
def test_patern():#pattern to test all 4 devices
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

def black():#sets everything to black
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

def animshowdelay(fan,index,R,G,B,delay):#do not use. shows 1 led and adds delay. replaced by the fps system
    setledupdate(fan,index,R,G,B)
    time.sleep(delay)

def anim_RGB():#simple animation
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

def anim_custom(R,G,B,speed=0.2):#simple animation
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

def anim1(R,G,B,speed=0.2):#simple animation
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

def setFans(index,R,G,B,delay):#sets specified led on all 3 fans and calling show() afterwards
    setled(0,index,R,G,B)
    setled(1,index,R,G,B)
    setled(2,index,R,G,B)
    show()
    time.sleep(delay)

def setFansNoShow(index,R,G,B):#sets specified led on all 3 fans without calling show()
    setled(0,index,R,G,B)
    setled(1,index,R,G,B)
    setled(2,index,R,G,B)

def hueshift(speed):#not working
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

def system_info(R,G,B,speed=0):#displays system vitals on fans



    cpu_usage = psutil.cpu_percent()
    cpu_time.append(int(cpu_usage))
    cpu_time.pop(0)
    cpu_usage = statistics.mean(cpu_time)



    ram_usage = psutil.virtual_memory()[2]
    if False:#alternative ram visualisation
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
    if True:#used ram visualisation
        color=min(1,max(0,scale(ram_usage,(20,30),(0,1))))
        setled(2,5,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(30,37),(0,1))))
        setled(2,4,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(30,37),(0,1))))
        setled(2,6,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(37,44),(0,1))))
        setled(2,3,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(37,44),(0,1))))
        setled(2,7,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(44,51),(0,1))))
        setled(2,2,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(44,51),(0,1))))
        setled(2,8,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(51,58),(0,1))))
        setled(2,1,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(51,58),(0,1))))
        setled(2,0,int(R*color),int(G*color),int(B*color))
        
        
        color=min(1,max(0,scale(ram_usage,(58,65),(0,1))))
        setled(1,5,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(65,72),(0,1))))
        setled(1,4,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(65,72),(0,1))))
        setled(1,6,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(72,79),(0,1))))
        setled(1,3,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(72,79),(0,1))))
        setled(1,7,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(79,86),(0,1))))
        setled(1,2,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(79,86),(0,1))))
        setled(1,8,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(86,93),(0,1))))
        setled(1,1,int(R*color),int(G*color),int(B*color))
        
        color=min(1,max(0,scale(ram_usage,(86,93),(0,1))))
        setled(1,0,int(R*color),int(G*color),int(B*color))
    if True:#cpu visualisation
        color=min(1,max(0,scale(cpu_usage,(0,20),(0,1))))
        setled(0,5,int(R*color),int(G*color),int(B*color))

        color=min(1,max(0,scale(cpu_usage,(20,30),(0,1))))
        setled(0,4,int(R*color),int(G*color),int(B*color))

        color=min(1,max(0,scale(cpu_usage,(30,40),(0,1))))
        setled(0,3,int(R*color),int(G*color),int(B*color))

        color=min(1,max(0,scale(cpu_usage,(40,50),(0,1))))
        setled(0,2,int(R*color),int(G*color),int(B*color))

        color=min(1,max(0,scale(cpu_usage,(50,60),(0,1))))
        setled(0,1,int(R*color),int(G*color),int(B*color))

        color=min(1,max(0,scale(cpu_usage,(60,70),(0,1))))
        setled(0,0,int(R*color),int(G*color),int(B*color))

        color=min(1,max(0,scale(cpu_usage,(70,80),(0,1))))
        setled(0,8,int(R*color),int(G*color),int(B*color))

        color=min(1,max(0,scale(cpu_usage,(80,90),(0,1))))
        setled(0,7,int(R*color),int(G*color),int(B*color))

        color=min(1,max(0,scale(cpu_usage,(90,100),(0,1))))
        setled(0,6,int(R*color),int(G*color),int(B*color))

        
    
    # print("cpu: ", cpu_usage, "   Ram: ",ram_usage, "   list: ",cpu_time)#shows vitals in console(optional)
    show()
    time.sleep(speed)
def meter(speed=0.1):#its a theme
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
def fps_limit(fps=20):#limits the rate at wich show is called
    endfps=time.time()
    global startfps
    frametime=(1/fps)-(endfps-startfps)
    print(frametime)
    time.sleep(max(0,frametime))
    if frametime<0:
        print("can`t keep up to framerate")
    startfps=time.time()

def main():#main loop controlling what scheme is displayed
    black()
    while True:
        global state
        global fps
        global gR
        global gG
        global gB
        
        if state==0:#state is written in gui()
            break
        elif state==1:
            fps = 10
            system_info(gR,gG,gB,0.01)
        elif state==2:
            fps = 1
            test_patern()
        elif state==3:
            fps = 20
            anim1(gR,gG,gB)
        elif state==4:
            fps = 20
            meter(0.0005)

#guiloop
def gui():
    window = sg.Window('Window Title', layout,no_titlebar=True,grab_anywhere=True,keep_on_top=True)#defining the gui window

    while True:
        global state
        global gR
        global gG
        global gB

        event, values = window.read()
        if event == 'exit':
            window.close()
            state=0
            break
        if event == 'close':
            window.hide()
            keyboard.wait("ctrl+alt+w")
            window.un_hide()
        if event == 'R' and not values['R']:#checking wrong input to rgb fields
            values['R']="0"
        if event == 'R' and values['R'] and values['R'][-1] not in ('0123456789'):
            window['R'].update(values['R'][:-1])
            values['R']=values['R'][:-1]
        if event == 'R' and not values['R']:
            values['R']="0"
        if event == 'R' and int(values['R'])>255:
            window['R'].update(values['R'][:-1])
            values['R']=values['R'][:-1]
        if event == 'R' and int(values['R'])<0:
            window['R'].update(values['R'][:-1])
            values['R']=values['R'][:-1]

        
        if event == 'G' and not values['G']:
            values['G']="0"
        if event == 'G' and values['G'] and values['G'][-1] not in ('0123456789'):
            window['G'].update(values['G'][:-1])
            values['G']=values['G'][:-1]
        if event == 'G' and not values['G']:
            values['G']="0"
        if event == 'G' and int(values['G'])>255:
            window['G'].update(values['G'][:-1])
            values['G']=values['G'][:-1]
        if event == 'G' and int(values['G'])<0:
            window['G'].update(values['G'][:-1])
            values['G']=values['G'][:-1]
        


        if event == 'B' and not values['B']:
            values['B']="0"
        if event == 'B' and values['B'] and values['B'][-1] not in ('0123456789'):
            window['B'].update(values['B'][:-1])
            values['B']=values['B'][:-1]
        if event == 'B' and not values['B']:
            values['B']="0"
        if event == 'B' and int(values['B'])>255:
            window['B'].update(values['B'][:-1])
            values['B']=values['B'][:-1]
        if event == 'B' and int(values['B'])<0:
            window['B'].update(values['B'][:-1])
            values['B']=values['B'][:-1]


        gR=int(values['R'])#setting global rgb values
        gG=int(values['G'])
        gB=int(values['B'])
        

        if event == 'System info':#setting rgb status. is read in main()
            state=1
        if event == 'test_pattern':
            state=2
        if event == 'anim1':
            state=3
        if event == 'anim2':
            state=4
#start multithreadding
if __name__ =="__main__":
    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=gui)

    t1.start()
    t2.start()