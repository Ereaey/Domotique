import socket

import sys
from math import *

def extract(data, key):
	e = data.find(key)
	f = data.find('\n', e)
	if e != -1 and f != -1:
		return data[e + len(key):f]
	else:
		return "Not find"

def treatment(data):
	target = extract(data, "target=")
	source = extract(data, "source=")
	device = extract(data, "device=")
	command = extract(data, "command=")
	print "Target : ", target
	print "Source : ", source
	print "Device : ", device
	print "Command : ", command

port = 5000

try:
	serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print "Problem Socket : Init"

listen_addr = ("", port)
try:
	serv.bind(listen_addr)
	print "Server start : port ", port
except socket.error:
	print "Problem Socket : Bind"

while True:
	data, addr = serv.recvfrom(1024)
	treatment(data)
	print data
