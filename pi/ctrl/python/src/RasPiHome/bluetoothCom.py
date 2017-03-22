import bluetooth


port 	= 1
bt_addr = None
bt_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)


###
#
# setup
#
# Parameter
#   bt_name        Name of a bluetooth device, thats
#
# Return
#   The address of the found device
####
def setup(bt_name):
    global bt_addr, bt_sock
    nearby_devices = bluetooth.discover_devices()

    for addr in nearby_devices:
        if bt_name == bluetooth.lookup_name(addr):
            bt_addr = addr
            break

    if bt_addr == None:
        return 1

    bt_sock.connect((bt_addr, 1))

    return bt_addr


# Used for sending data
def send(message):
    global bt_sock
    bt_sock.send(message)


# Used for receiving data
def recv(size):
    global bt_sock
    return bt_sock.recv(size)



