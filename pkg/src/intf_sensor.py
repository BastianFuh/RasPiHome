import spidev
import RPi.GPIO as GPIO

spi = None



# reads data from a MCP3204 ic over the spi Interface
def read(channel):
    spi = spidev.SpiDev()
    spi.open(0,0)


    GPIO.setmode(GPIO.BOARD)

    # this gpio pin is the CS for the spi interface, usually you don't have to do this
    # this is just necessary here, because the pcb, used in this project, was design like this,
    # where a different pin was used for the CS
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, GPIO.HIGH)

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
        GPIO.output(11, GPIO.LOW)
        data = spi.xfer([ 6, channel << 6, 0])
        GPIO.output(11, GPIO.HIGH)
        #
        # X = not important
        # ? = data
        # returned data = [XXXX XXXX] [XXXX ????] [???? ????]
        #
        return (((data[1] & 15 ) << 8) + data[2])

    finally:
        spi.close()