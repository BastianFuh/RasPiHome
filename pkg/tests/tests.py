from ..src import intf_sensor
import time

while True:
    print "Channel 0", intf_sensor.readChannel(0)
    print "Channel 1", intf_sensor.readChannel(1)
    time.sleep(5)