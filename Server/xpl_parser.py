class XPL_Parser:
	def __init__(self, data):
		self.data = data
		self.type = self.extractType()
		self.protocol = self.extractProtocol()
		
	def getProtocol(self):
		return self.protocol

	def getType(self):
		return self.type

	def getDevice(self):
		return self.extract("device")

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