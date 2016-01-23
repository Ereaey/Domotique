import os
import subprocess
import xpl
import sys
from xpl_parser import *
from xpl_exec import *
class XPL_Treatment:
	def __init__(self, data):
		self.parser = XPL_Parser(data)
		for l in os.listdir("scripts/cond/"):
			file = open('scripts/cond/' + l, "r")
			self.data = file.read()
			if self.verif_protocol() == True:
				if self.extract("header") == "sensor.basic" and self.extract("device") == self.parser.getDevice() and self.extract("type") == self.parser.getTypeData() and self.extract("current") == self.parser.getCurrent():
					self.exec_file(self.extract("action"))
				elif self.extract("header") == "datetime.basic" and self.extract("time") == self.parser.getTime():
					self.exec_file(self.extract("action"))
				elif self.extract("header") == "dawndusk.basic" and self.extract("status") == self.parser.getStatus():
					self.exec_file(self.extract("action"))
			file.close()

	def verif_protocol(self):
		if self.extract("header") == self.parser.getProtocol():
			return True
		else:
			return False

	def exec_file(self, path):
		extension = path.split('.')[-1]
		if extension == "py":
			subprocess.Popen(['python', 'scripts/exec/' + path])
		else:
			XPL_Exec('scripts/exec/' + path)
		print "Exec file : ", path

	def extract(self, key):
		key += "="
		e = self.data.find(key)
		f = self.data.find('\n', e)
		if e != -1 and f != -1:
			return self.data[e + len(key):f]
		else:
			return "Not found"