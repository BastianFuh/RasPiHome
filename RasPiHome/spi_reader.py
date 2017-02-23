import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)

try:
    while True:
        data = spi.xfer2([ 6, 0, 0])
        time.sleep(0.1)

        value = (data[0] << 6) + data[1]

        print "Ausgelesener Wert: ", value

finally:
    spi.close()