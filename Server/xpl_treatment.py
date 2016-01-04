import os
import xpl
import sys
from xpl_parser import *

class XPL_Treatment:
	def __init__(self, data):
		self.parser = XPL_Parser(data)
		for l in os.listdir("scripts/cond/"):
			print l
			file = open('scripts/cond/' + l, "r")
			self.data = file.read()
			if self.verif_protocol() == True:
				if self.extract("header") == "sensor.basic":
					if self.extract("device") == self.parser.getDevice():
						if self.extract("type") == self.parser.getTypeData():
							if self.extract("current") == self.parser.getCurrent():
								self.exec_file(self.extract("action"))
			else:
				print "nop"
			file.close()

	def verif_protocol(self):
		if self.extract("header") == self.parser.getProtocol():
			return True
		else:
			return False

	def exec_file(self, path):
		print path

	def extract(self, key):
		key += "="
		e = self.data.find(key)
		f = self.data.find('\n', e)
		if e != -1 and f != -1:
			return self.data[e + len(key):f]
		else:
			return "Not find"

x = XPL_Treatment(sys.argv[1])