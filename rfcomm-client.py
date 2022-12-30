from bluetooth import *

server_addr = 'DC:A6:32:95:79:42'
puerto = 3

sock = BluetoothSocket(RFCOMM)
sock.connect((server_addr, puerto))

sock.send("Hola!")

sock.close()
