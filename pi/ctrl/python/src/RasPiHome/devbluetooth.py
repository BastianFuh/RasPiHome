import bluetooth

## @package src.RasPiHome.devbluetooth
#  Wrapper for the bluetooth module.

## Wrapper around the bluetooth module
class DevBluetooth:
    def __init__(self):
        ##The bt Socket
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        ## The address of the connected bluetooth device
        self.addr = None
        ## The name of the connected bluetooth device
        self.name = ""
        ## The amount of data which will be received
        self.recv_size = 32

    def __del__(self):
        self.sock.close()


    ## Creates the bt socket for the communication
    #
    # Takes the given name of the device and searches for it,
    # if a device with the name is found, it will store its
    # address and connects to it.
    #
    # @param bt_name the name of the bluetooth device
    def begin(self, bt_name):
        self.name = bt_name

        nearby_devices = bluetooth.discover_devices()

        for addr in nearby_devices:
            if bt_name == bluetooth.lookup_name(addr):
                bt_addr = addr
                break

        if bt_addr is None:
            return 1

        self.sock.connect((bt_addr, bluetooth.get_available_port(bluetooth.RFCOMM)))

    ## Returns the addr of the connected device
    # @return address of connected device
    def get_addr(self):
        return self.addr

    ## Returns the name of the device
    # @returns name of connected device
    def get_name(self):
        return self.name

    ## Sends a message to the connected device
    # @param message
    def send(self, message):
        self.sock.send(message)

    ## Sets the size thats read from the device.
    # @param size The amount of Bytes that should be read
    def set_recv_size(self, size):
        self.recv_size = size

    ## Receives data from the connected device
    # @return return the recv message
    def recv(self):
        return self.sock.recv(self.recv_size)

    ## Reveives a certain amount of data from the connected device
    # @param size the amount of data that should be read
    #
    # @return the read message
    def rec(self, size):
        return self.sock.recv(size)
