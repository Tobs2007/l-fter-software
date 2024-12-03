import globals
globals.init()
import fans
import phue
import time
print("load")
time.sleep(1)
fans.startfans()
# phue.debug()
phue.main()
print("hi")