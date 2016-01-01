import sys

class XPL_Parser:
	def __init__(self, data):
		self.data = data
		self.type = self.extractType()
		self.protocol = self.extractProtocol()

	def setData(self, data):
		self.data = data
		self.type = self.extractType()
		self.protocol = self.extractProtocol()
		
	def getProtocol(self):
		return self.protocol

	def getType(self):
		return self.type

	def getDevice(self):
		return self.extract("device")

	def getCommand(self):
		return self.extract("command")

	def getUnit(self):
		return self.extract("unit")

	def getAddress(self):
		return self.extract("address")

	def getLevel(self):
		return self.extract("level")

	def getHouse(self):
		return self.extract("house")

	def getNode(self):
		return self.extract("node")

	def getMode(self):
		return self.extract("mode")

	def getText(self):
		return self.extract("text")

	def getStatus(self):
		return self.extract("status")

	def extractType(self):
		f = self.data.find('\n', 0)
		if f != -1:
			return self.data[0:f]
		else:
			return "Not find"

	def extractProtocol(self):
		e = self.data.find("}")
		f = self.data.find("{", e)
		if e != -1 and f != -1:
			return self.data[e + 2:f - 1]
		else:
			return "Not find"

	def extract(self, key):
		key += "="
		e = self.data.find(key)
		f = self.data.find('\n', e)
		if e != -1 and f != -1:
			return self.data[e + len(key):f]
		else:
			return "Not find"

if __name__ == '__main__':
	c = XPL_Parser(sys.argv[1])
	print c.getProtocol()
	print c.getType()
	print c.extract(sys.argv[2])