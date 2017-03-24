#!/usr/bin/python

import sys
import time

import devi2c

## @package src.RasPiHome.actuatorctl
# Commandline Programm that can controll the actuators.
# This tool is used by the website to control the actuators,
# but it can used as a debug tool too.

if len(sys.argv) <= 1:
    sys.exit(-1)

addr = int(sys.argv[1])
port = int(sys.argv[2])
pos  = int(sys.argv[3])

devi2c.writeData(addr, port, [pos])
time.sleep(3)

sys.exit(0)
