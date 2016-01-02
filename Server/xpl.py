class XPL_Msg:
	def __init__(self, source, target):
		self.source = source
		self.target = target
		self.header = self.generate_header()
		self.body = ""
		self.type = ""
	def homeeasy(self, address, unit, command):
		self.type = "homeeasy.basic"
		self.add("address", address)
		self.add("unit", unit)	
		self.add("command", command)	
	def x10(self, device, command):
		self.type = "x10.basic"
		self.add("device", device)
		self.add("command", command)		
	def x10security(self, device, command):
		self.type = "x10.security"
		self.add("device", device)
		self.add("command", command)
	def xpl(self, device, command):
		self.type = "xpl.basic"
		self.add("device", device)
		self.add("command", command)
	def zwave(self, device, command):
		self.self.type = "zwave.basic"
		self.add("node", device)
		self.add("command", command)
	def add(self, key, value):
		self.body += key + "=" + value + '\n'
	def setType(self, type):
		self.type = type

	def generate_header(self):
		header = "xpl-cmnd"
		header += '\n'
		header += "{"
		header += '\n'
		header += "hop=1"
		header += '\n'
		header += "source=" + self.source
		header += '\n'
		header += "target=" + self.target
		header += '\n'
		header += "}"
		header += '\n'
		return header
	def generate_data(self):
		data = self.type
		data += '\n'
		data += "{"
		data += '\n'
		data += self.body
		data += '}'
		return data
	def getData(self):
		d = self.generate_header()
		d += self.generate_data()
		return d

if __name__ == '__main__':
	x = XPL_Msg("dqsd", "abc")
	x.homeeasy("b1", "2", "on")
	print x.getData()