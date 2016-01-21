import socket
import datetime
import sys
import sqlite3
from xpl_parser import *
from xpl_treatment import *
from xpl_sender import *
from math import * 

def treatment(data):
	x = XPL_Parser(data)
	commandName = x.getType()
	protocol = x.getProtocol()
	print "Command name : ", commandName 
	print "Protocol : ", protocol
port = 5000

try:
	serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print "Problem Socket : Init"
	sys.exit(0)

listen_addr = ("", port)
try:
	serv.bind(listen_addr)
	print "Server start : port ", port
except socket.error:
	print "Problem Socket : Bind"
	sys.exit(0)

print "Waiting to receive message"

while True:
	try:
		file = open("log.txt", "aw")
		data, addr = serv.recvfrom(1024)
		treatment(data)
		date = datetime.datetime.today()
		file.write("%s : %s \n%s\n" % (date, addr[0], data))
		file.close()
		XPL_Treatment(data)
		print "Message received"
		#serv.sendto('ack', addr)

	except KeyboardInterrupt:
		print "Server Close"
		sys.exit(0)