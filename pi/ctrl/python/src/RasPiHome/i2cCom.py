import smbus

bus = smbus.SMBus(1)

def setup():
	global bus 
	bus = smbus.SMBus(1)


# ----------------------------------------------------------------------
# Writes data to a certain device over the i2c bus
#  
# addr     	- the i2c address of the device
# port	 	- port of the interface
# value		- additional information in an array 
# ----------------------------------------------------------------------

def writeData(addr, port, val):
	try:
		bus.write_i2c_block_data(addr, port, val)
	except IOError, err:
		return -1
	return 0


# ----------------------------------------------------------------------
# Read data from a certain device over the i2c bus
#
# addr		- the i2c address of the device
# port	 	- port of the interface
# ----------------------------------------------------------------------

def readData(addr, port):
	data  	= 0
	counter = 0

	try:
		buffer = bus.read_i2c_block_data(addr, port)

		length = buffer[0]
		while counter < length:
			data += ( buffer[counter + 2] << (8 * length - 1 - counter ))
	except IOError, err:
		return -1
	return data



