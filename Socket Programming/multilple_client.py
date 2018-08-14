# multiple_client.py
# To connect multiple client to a server.

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def connection():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("hi you are connected", "utf8"))

        
HOST = ''
PORT = 3000
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
SERVER.listen(5)
print("Waiting for connection...")
ACCEPT_THREAD = Thread(target=connection())
ACCEPT_THREAD.start()
ACCEPT_THREAD.join()
SERVER.close()
