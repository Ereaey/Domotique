import socket
import datetime
import sys
import os
from math import *

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

file = open("log.txt", "w")

while True:
	data, addr = serv.recvfrom(1024)
	date = datetime.datetime.today()
	print "{} : {}".format(date, addr[0])
	print data
	file.write("%s : %s \n%s\n" % (date, addr[0], data))

