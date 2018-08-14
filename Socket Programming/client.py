# client.py
# A simple client requenst and response.

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input('enter host name:')
port=int(input('enter port:'))
print(host)
s.connect((socket.gethostname(), port))
msg = 'Pls let me connect'
s.send(msg.encode())
tm = s.recv(1024)                                     
s.close()
print(tm.decode('UTF-8'))