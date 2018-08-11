# host_ip.py
# Retrive ip from the host name.
import socket
try:
    host_name = input('Enter host name')
    host_ip = socket.gethostbyname(host_name)
    print("Hostname :  ", host_name)
    print("IP : ", host_ip)
except:
    print("Unable to get Hostname and IP")

