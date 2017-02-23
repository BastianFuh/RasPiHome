from .context import RasPiHome
from RasPiHome import spi_reader


while True:
    print "Channel 0", spi_reader.readChannel(0)
    print "Channel 1", spi_reader.readChannel(1)