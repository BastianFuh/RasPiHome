import time

from ..RasPiHome import devbluetooth

devbluetooth.setup("")

while 1:
    devbluetooth.send("Test")

    time.sleep(1)
