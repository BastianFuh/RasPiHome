import smbus
import time

# CONST - FUNCTION CODES 


DEBUG = 0


# -- READ



# -- WRITE

# SERVO START
SERVO_WRITE = 128
# SERVO END


#

bus = None

bus = smbus.SMBus(1)

def setup():
	global bus 
	bus = smbus.SMBus(1)

# could be removed, because it may be not needed
def writeByte(addr, fun_code):
	try:
		bus.write_byte(addr, value)
	except IOError, err:
		return -1
	return 0	


def readByte():
	None



# ----------------------------------------------------------------------
# Writes data to a certain device over the i2c bus
#  
# addr     	- the i2c address of the device
# fun_code 	- code of the function that should be executed
#	           see "CONST - FUNCTION CODES" at the beginning of the code
# value		- additional information in an array 
# ----------------------------------------------------------------------

def writeData(addr, fun_code, val):
	try:
		bus.write_i2c_block_data(addr, fun_code, val)
	except IOError, err:
		return -1
	return 0

	
# ----------------------------------------------------------------------
# Read data from a certain device over the i2c bus
#
# addr		- the i2c address of the device
# fun_code 	- code of the function that should be executed
#	           see "CONST - FUNCTION CODES" at the beginning of the code
# ----------------------------------------------------------------------

def readData(addr, fun_code):
	try:
		data = bus.read_i2c_block_data(addr, fun_code)
		
	except IOError, err:
		return -1
	return data


while True:
	time.sleep(5)
	
	tmp = bus.read_i2c_block_data(0x08, 2)
	tmp = bus.read_i2c_block_data(0x08, 2)
	print "Humidity: ", (tmp[0] << 8) + tmp[1]
	

	tmp = bus.read_i2c_block_data(0x08, 1)
	print "Temperature: ", (tmp[0] << 8) + tmp[1]  
	
	
