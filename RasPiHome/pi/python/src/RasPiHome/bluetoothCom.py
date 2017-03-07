import bluetooth


port 	= 1
bt_addr = None
bt_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)


# returns the address of the found devices
def setup(bt_name):
	
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
	bt_sock.send(message)


# Used for receiving data
def recv(size):
	return bt_sock.recv(size)



