#!/usr/bin/env python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect(('115.28.161.90',8001))
sock.connect(('localhost',7556))
import time
time.sleep(2)
#sock.send('1')
while True:
    print sock.recv(1024)
sock.close()
