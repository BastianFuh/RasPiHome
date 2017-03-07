from ..RasPiHome import i2cCom as i2c
import time

i2c.setup()

addr = 0x08

while True:
	time.sleep(1)
	i2c.writeData(addr, i2c.DEBUG, [256,157,755, 196])
