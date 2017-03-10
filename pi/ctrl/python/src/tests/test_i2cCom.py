from ..RasPiHome import i2cCom as i2c
from ..lib import libCom

import time



i2c.setup()

addr = 0x08

while True:
	time.sleep(5)
	i2c.writeData(addr, libCom.DEBUG, [256,157,755, 196])

	print "Humidity: ", i2c.readData(addr, 2)

	print "Temperature: ", i2c.readData(addr, 2)