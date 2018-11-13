# Server.py
# A simple Server requenst and response.

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()                           
port = 2645                                           
s.bind((host, port))
s.listen(5)
while True:
    clientsocket,addr = s.accept()
    print("Got a connection from %s" % str(addr))
    msg = 'You are connected'
    clientsocket.send(msg.encode('UTF-8'))
    clientsocket.close()