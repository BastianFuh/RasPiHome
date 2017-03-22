#!/usr/bin/python

import sys
import time

import i2cCom

if len(sys.argv) <= 1:
    sys.exit(-1)

addr = int(sys.argv[1])
port = int(sys.argv[2])
pos  = int(sys.argv[3])

i2cCom.writeData(addr, port, [pos])
time.sleep(3)

sys.exit(0)
