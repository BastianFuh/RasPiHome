import spidev
import RPi.GPIO as GPIO

## reads the data from a MCP3204 ic over the spi Interface.

##

spi = spidev.SpiDev()

## open the connection to the spi bus
def begin():
    global spi
    spi.open(0, 0)

def stop():
    spi.close()


## @package src.RasPiHome.devspi
# sends three bytes of data to the spi slave.
#
# X = not important
# first byte = XXXX X110
#   - the third bit is the start bit,
#   - the second bit determines, if the data is read differential or single-ended, here single-ended
#   - the first bit, is the third bit, that determines the channel to read from, this
#     one is not needed, because the MCP3204 has only four channels, not like than the MCP3208,
#     which has eight
#
# second byte = [D1][D0]XX XXXX
#   D1 and D0 are used to select the channel to read from
#
# @param channel the channel on the ic that should be read from
def read(channel):

    try:

        data_send = [6, channel, 0]
        print "Send Data: ", data_send

        data = spi.xfer(data_send)
        print "Recv Data: ", data

        #
        # X = not important
        # ? = data
        # returned data = [XXXX XXXX] [XXXX ????] [???? ????]
        #
        return ((data[1] & 15) << 8) + data[2]
    except IOError:
        pass
