# client.py  
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2645
s.connect((host, port))
anil = 'Here is your file'
s.send(anil.encode())
createFile = open("b.jpg", "wb")
data = s.recv(1024)
while data:
    createFile.write(data)
    data = s.recv(1024)
createFile.close()
s.close()
