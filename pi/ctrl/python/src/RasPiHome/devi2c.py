import smbus
import math

## @package src.RasPiHome.devi2c
# Wrapper around the smbus module.

## Wrapper for the python smbus module.


bus = smbus.SMBus(1)


## writes data to a specified slave
#
# @param addr the i2c address of the slave
# @parma port port of the interface
# @param data additional information in an array
def write(addr, port, data):
    global bus
    try:
        bus.write_i2c_block_data(addr, port, data)
    except IOError:
        return -1
    return None


## Reads data from a slave
#
# converts the received number in to an integer/float and returns it
#
# @param addr the i2c address of the device
# @param port port of the interface
#
# @return returns the received number converted
def read_sensor(addr, port):
    global bus
    data = 0
    counter = 0
    try:
        recvBuffer = bus.read_i2c_block_data(addr, port)
        length = recvBuffer[0]
        while counter < length:
            data += (recvBuffer[counter + 2] << (8 * ((length - 1) - counter)))
            counter += 1
    except IOError:
        return -1
    return data / math.pow(10, recvBuffer[1])


## Reads data from a i2c Device
#
# Arguments
# 	addr		- the i2c address of the device
# 	port	 	- port of the interface
#
# @return the received data as an array
def read_raw_data(addr, port):
    global bus
    try:
        data = bus.read_i2c_block_data(addr, port)
    except IOError:
        return -1
    return data
