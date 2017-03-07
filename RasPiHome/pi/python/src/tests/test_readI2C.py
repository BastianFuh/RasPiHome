from ..RasPiHome import i2cCom as i2c
import time

i2c.setup()

addr = 0x08

while True:
	time.sleep(5)
	print i2c.readData(addr, 1)
