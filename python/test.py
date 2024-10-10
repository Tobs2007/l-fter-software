import serial
import time
import colorsys
while True:
    print(str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5]))
    time.sleep(1)