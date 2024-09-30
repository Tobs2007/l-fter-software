#rot=255
#grün=96
#blau=160

import serial
import time

arduino = serial.Serial(port='COM13',   baudrate=250000, timeout=1)
time.sleep(0.5)

def setled(fan,index,R,G,B):
    arduino.write(bytes(fan,   'utf-8'))
    time.sleep(0.002)
    arduino.write(bytes(index,   'utf-8'))
    time.sleep(0.002)
    arduino.write(bytes(R,   'utf-8'))
    time.sleep(0.002)
    arduino.write(bytes(G,   'utf-8'))
    time.sleep(0.002)
    arduino.write(bytes(B,   'utf-8'))
    time.sleep(0.04)


setled("0","0","0","0","0")
setled("0","1","0","0","0")
setled("0","2","0","0","0")
setled("0","3","0","0","0")
setled("0","4","0","0","0")
setled("0","5","0","0","0")
setled("0","6","0","0","0")
setled("0","7","0","0","0")
setled("0","8","0","0","0")

setled("1","0","0","0","0")
setled("1","1","0","0","0")
setled("1","2","0","0","0")
setled("1","3","0","0","0")
setled("1","4","0","0","0")
setled("1","5","0","0","0")
setled("1","6","0","0","0")
setled("1","7","0","0","0")
setled("1","8","0","0","0")

setled("2","0","0","0","0")
setled("2","1","0","0","0")
setled("2","2","0","0","0")
setled("2","3","0","0","0")
setled("2","4","0","0","0")
setled("2","5","0","0","0")
setled("2","6","0","0","0")
setled("2","7","0","0","0")
setled("2","8","0","0","0")
time.sleep(10)