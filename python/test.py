import serial
import time
arduino = serial.Serial(port='COM13',   baudrate=115200, timeout=1)
time.sleep(5)
def write_read(x):
    arduino.write(bytes(x,   'utf-8'))
    time.sleep(0.05)
    print(bytes(x,   'utf-8'))


write_read("2")
#time.sleep(0.5)
write_read("1")
#time.sleep(0.5)
write_read("255")
#time.sleep(0.5)
write_read("255")
# time.sleep(0.5)
write_read("255")
time.sleep(5)