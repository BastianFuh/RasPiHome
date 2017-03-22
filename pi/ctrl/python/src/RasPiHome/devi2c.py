import smbus
import math

bus = smbus.SMBus(1)


def setup():
    global bus
    bus = smbus.SMBus(1)

""""
* writeData
*
* Writes data to a certain i2c Device
*
*
*
* addr     	- the i2c address of the device
* port	 	- port of the interface
* value		- additional information in an array
"""

def writeData(addr, port, val):
    try:
        bus.write_i2c_block_data(addr, port, val)
    except IOError:
        return -1
    return None


"""
* readSensor
*
* Reads data from a i2c Device
* converts the number in to an integer/float and returns it
*
* Arguments
* 	addr		- the i2c address of the device
* 	port	 	- port of the interface
*
* Return
*	Returns the converted number
*
"""

# !!! rename to readDigitalSensor, and create readAnalogSensor and readI2C !!!


def readSensor(addr, port):
    data = 0
    counter = 0
    recvBuffer 	= None
    try:
        recvBuffer = bus.read_i2c_block_data(addr, port)
        length = recvBuffer[0]
        while counter < length:
            data += (recvBuffer[counter + 2] << (8 * ((length - 1) - counter)))
            counter += 1
    except IOError:
        return -1
    return data / math.pow( 10, recvBuffer[1])


"""
* readRawData
*
* Reads data from a i2c Device
*
* Arguments
* 	addr		- the i2c address of the device
* 	port	 	- port of the interface
*
* Return
* 	Returns the received data as an array
*
"""


def readRawData(addr, port):
    data = None

    try:
        data = bus.read_i2c_block_data(addr, port)
    except IOError:
        return -1
    return data
