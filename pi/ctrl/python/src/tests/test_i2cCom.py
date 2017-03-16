from ..RasPiHome import i2cCom as i2c
from ..lib import libCom

import time


i2c.setup()

addr = 0x08

state = 0

#i2c.writeData(addr, 0x0C, [150])


while True:
    time.sleep(5)
    # i2c.writeData(addr, libCom.DEBUG, [256,157,755, 196])

    print "Temperature ", i2c.readData(addr, 0x01)
    print "Humidity ", i2c.readData(addr, 0x02)
    light = i2c.readData(addr, 0x03)

    print "Light: ", light


    if light > 700 and state == 1 and light != -1:
        print "Open Door"
        i2c.writeData(addr, 0x0C, [180])
        time.sleep(10)
        state = 0

    if light < 400 and state == 0 and light != -1:
        print "Close Door"
        i2c.writeData(addr, 0x0C, [110])
        time.sleep(10)
        state = 1
