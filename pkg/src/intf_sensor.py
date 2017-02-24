import spidev

# reads the data from a MCP3204 ic over the spi Interface
def read(channel):
    spi = spidev.SpiDev()
    spi.open(0,0)

    try:
        #
        # reads the data
        # three bytes of date are being send
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
        data = spi.xfer2([ 6, channel << 6, 0])

        #
        # X = not important
        # ? = data
        # returned data = [XXXX XXXX] [XXXX ????] [???? ????]
        #
        return (((data[1] & 15 ) << 8) + data[2])

    finally:
        spi.close()