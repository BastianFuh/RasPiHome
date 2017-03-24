import time

from ..RasPiHome import devi2c as i2c


i2c.setup()

addr = 0x08

state = 0

#i2c.writeData(addr, 0x0C, [150])


while True:
    time.sleep(5)

    print "Temperature ", i2c.readSensor(addr, 0x10)
    print "Humidity ", i2c.readSensor(addr, 0x25)
    light = i2c.readSensor(addr, 0x30)

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
