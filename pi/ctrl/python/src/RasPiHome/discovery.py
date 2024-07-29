"""
Discovers the Interfaces connected to the I2C Bus
and stores these information in file with a json formats

#- WIP -#
Currently deletes the entire folder before every
search and then recreates it, which is not realy
efficient and could be change, so that its checks
if the address are still available, if the
ports have changed and if this is the case it
should take appropriated actions, so that just
these files are deleted, that are either not
needed anymore, e.g. an address is gone or has
changed so the folder may be deleted, or has
false information in them, e.g. a port changed.

It may not result in the desired effect, when
you check for all of these things, because it may
creates a bigger overhead, then deleting everything
and recreating it. And if it is not more efficient
i see no point in implementing it.
"""

import json
import os
import shutil

import devi2c
from lib import libCom

## @package src.RasPiHome.discovery
# Discovers the Interfacs connected tot the i2c bus.
#
# Goes through all the possible address to find the connected slaves on the bus.
# If a slave was found it will save the information about it into a file in json
# format.
#

devi2c.begin()

dirPath = "/opt/RasPiHome/dev/"
filePath = "/opt/RasPiHome/dev/"
try:
    shutil.rmtree("/opt/RasPiHome/dev")
except OSError:
    pass
os.mkdir("/opt/RasPiHome/dev")

for addr in range(0x08, 0x78):
    try:
        data = devi2c.read_raw_data(addr, libCom.PORT_DISCOVERY)

        if data[0] != 0:
            os.mkdir(dirPath+str(hex(addr)))

            numSensor = data[0]
            print "Found address " + hex(addr) + " with Ports"

            for i in range(0, numSensor):

                data = devi2c.read_raw_data(addr, i)

                jsonF = {"conn_type": data[0],
                         "spec": data[1],
                         "conn": {
                             "addr": addr,
                             "port": data[2]
                         }
                         }
                print jsonF
                print "Saved in file: " + filePath + str(hex(addr)) + "/" + str(hex(data[2])) + ".json"
                with open(filePath + str(hex(addr)) + "/" + str(hex(data[2])) + ".json", 'w') as f:
                    json.dump(jsonF, f)

            if devi2c.read_raw_data(addr, libCom.PORT_DISCOVERY) == -1:
                print "Connection wasn't closed correctly"
    except TypeError:
        pass
