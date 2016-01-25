import socket
import datetime
import sys
import RPi.GPIO as GPIO
from xpl_parser import *

sys.stdout.flush()

port = 5001
GPIO.setMode(GPIO.BOARD)
GPIO.setup(17, GPIO.OUT)

try:
	serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print "Problem Socket : Init"
	sys.stdout.flush()
	sys.exit(0)

listen_addr = ("", port)
try:
	serv.bind(listen_addr)
	print "Server start : port ", port
except socket.error:
	print "Problem Socket : Bind"
	sys.stdout.flush()
	sys.exit(0)

print "Waiting to receive message"
sys.stdout.flush()

while True:
	try:
		file = open("log.txt", "aw")
		data, addr = serv.recvfrom(1024)
		x = XPL_Parser(data)
		commandName = x.getType()
		protocol = x.getProtocol()
		print "Command name : ", commandName 
		print "Protocol : ", protocol
		if x.getType() == "control.basic":
			if x.getDevice() == "M1":
				if x.getCurrent() == "on":
					GPIO.output(17, GPIO.HIGH)
				elif x.getCurrent() == "off":
					GPIO.output(17, GPIO.LOW)
		date = datetime.datetime.today()
		file.write("%s : %s \n%s\n" % (date, addr[0], data))
		file.close()
		
		print "Message received"
		sys.stdout.flush()
		
	except KeyboardInterrupt:
		print "Server Close"
		sys.stdout.flush()
		sys.exit(0)