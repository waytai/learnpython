#!/usr/bin/env python
import socket
import time
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('localhost',7556))
sock.listen(5)
connection,address = sock.accept()
print "client ip is "
print address
connection.settimeout(5)
while True:
    try:
        connection.send('welcome to python server!')
        time.sleep(2)
    except socket.timeout:
        print 'time out'
        connection.close()
