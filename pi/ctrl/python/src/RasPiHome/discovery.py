"""

Discovers the Interfaces connected to the I2C Bus
and stores them in Json files

#- WIP -#
Currently deletes the entire folder before every
search and then recreates it, which is not realy
nice and could be change, so that its checks
if the address are still available and if the
ports have changed and if this is the case it
should take appropriated actions, so that just
these files are deleted, that are either not
needed anymore, e.g. an address is gone or has
changed so the folder may be deleted, or have
false information in them, e.g. a port changed.

It may not result in the desired effect, when
you check for all of these things, it may even
create a bigger overhead, then deleting everything
and recreating it.

"""

import time

import json
import os
import shutil

import devi2c as i2c
from ..lib import libCom

i2c.setup()

jsonF = None
numSensor = 0
data = 0

dirPath = "/opt/RasPiHome/dev/"
filePath = "/opt/RasPiHome/dev/"
try:
    shutil.rmtree("/opt/RasPiHome/dev")
except OSError:
    pass
os.mkdir("/opt/RasPiHome/dev")

for addr in range(0x08, 0x78):
    try:

        data = i2c.readRawData(addr, libCom.PORT_DISCOVERY)

        if data[0] != 0:
            os.mkdir(dirPath+str(hex(addr)))

            numSensor = data[0]
            print "Found address " + hex(addr) + " with Ports"
            for i in range(0, numSensor):

                data = i2c.readRawData(addr, i)

                jsonF = {"type": data[0],
                         "spec": data[0],
                         "conn": {
                             "addr": addr,
                             "port": data[1]
                         }
                         }
                print jsonF
                print "Saved in file: " + filePath + str(hex(addr)) + "/" + str(data[1]) + ".json"
                with open(filePath + str(hex(addr)) + "/" + str(hex(data[1])) + ".json", 'w') as f:
                    json.dump(jsonF, f, indent=4)

            if i2c.readRawData(addr, libCom.PORT_DISCOVERY) == -1:
                print "Connection wasn't closed correctly"
    except TypeError:
        pass




