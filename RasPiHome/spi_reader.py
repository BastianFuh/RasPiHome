import spidev


def readChannel(channel):
    spi = spidev.SpiDev()
    spi.open(0,0)

    try:

        data = spi.xfer2([ 6, channel << 6, 0])
        return (((data[1] & 15 ) << 8) + data[2])

    finally:
        spi.close()