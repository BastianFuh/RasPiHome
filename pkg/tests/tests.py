from ..src import intf_sensor
import time


intf_sensor.setup()

while True:
    print "Channel 0", intf_sensor.read(0)
    print "Channel 1", intf_sensor.read(1)
    time.sleep(5)