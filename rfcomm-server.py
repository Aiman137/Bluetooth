from bluetooth import *

puerto = 3
backlog = 3

server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("",puerto))
server_sock.listen(backlog)

client_sock, client_info = server_sock.accept()
print("Conexión aceptada de ",client_info)

data = client_info.recv(1024)
print("Recibido: ", data)

client_sock.close()
server_sock.close()
