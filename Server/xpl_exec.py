import socket
import datetime
import sys
import os
from xpl import *
from xpl_sender import *

class XPL_Exec:
	def __init__(self, path):
		self.data = XPL_Msg("server.event", "*")
		file = open(path, "r")
		for line in file:
			line = line.replace('\n', '')
			d = line.split("=")
			if d[0] == "header":
				self.data.setType(d[1])
			else:
				self.data.add(d[0], d[1])
		file.close()
		self.send()

	def send(self):
		s = XPL_Sender(5001)
		s.send(self.data.getData())