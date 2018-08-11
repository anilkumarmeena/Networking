# file_server.py  
# simple file sender to client.

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2645
s.bind((host, port))
s.listen(5)
while True:
    clientsocket, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    readByte = open('a.jpg', "rb")
    data = readByte.read()
    print(type(data))
    while data:
        clientsocket.send(data)
        data = readByte.read()
    readByte.close()
    clientsocket.close()
    s.close()
