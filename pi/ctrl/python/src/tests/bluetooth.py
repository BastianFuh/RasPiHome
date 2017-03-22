import time

from ..RasPiHome import bluetoothCom

bluetoothCom.setup("HC-05-MASTER-1")

while 1:
    bluetoothCom.send("Test")

    time.sleep(1)
