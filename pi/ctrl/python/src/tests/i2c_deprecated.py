from ..RasPiHome import devi2c as i2c
import time

i2c.setup()

addr = 0x08

while True:
	time.sleep(5)





while True:
	time.sleep(5)

	tmp = bus.read_i2c_block_data(0x08, 2)
	tmp = bus.read_i2c_block_data(0x08, 2)
	print "Humidity: ", (tmp[0] << 8) + tmp[1]

	tmp = bus.read_i2c_block_data(0x08, 1)
	print "Temperature: ", (tmp[0] << 8) + tmp[1]