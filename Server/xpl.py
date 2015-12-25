'''
Types de messages possibles pour l'instant à faire :

OSD :
osd.basic
	write
		command = write
		text = tesdsqdsqd
	clear
		command = clear
homeeasy :
homeeasy.basic : controle chacon
	on/off
		command = on/off : on = 0, off = 1
		adress = 
		unit =
	preset
		command = preset
		level = (1-15)
		adress = 
		unit =
x10
x10.basic
	command =
	device = 
	house = 
	[level = ]
	[data1 = ]
	[data2 = ]
XPL
control.basic (Multiprise)
	command = on/off
	device = 

zwave
zwave.basic
à voir, on, off, level
'''
class XPL:
	def __init__(self, source, target):
		self.source = source
		self.target = target
	def homeeasy(self, address, unit, command):
		self.type = "homeeasy.basic"
		self.address = address
		self.unit = unit
		self.command = command
	def x10(self, device, command):
		self.type = "x10.basic"
		self.device = device
		self.command = command
	def x10security(self, device, command):
		self.type = "x10.security"
		self.device = device
		self.command = command
	def xpl(self, device, command):
		self.type = "xpl.basic"
		self.device = device
		self.command = command
	def zwave(self, device, command)
		self.type = "zwave.basic"
		self.device = device
		self.command = command

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
		if self.type == "x10.basic" or self.type == "x10.security":
			data += "device=" + self.device
			data += '\n'
			data += "command=" + self.command
			data += '\n'
		elif self.type == "xpl.basic":
			data += "device=" + self.device
			data += '\n'
			data += "command=" + self.command
			data += '\n'
		elif self.type == "homeeasy.basic":
			data += "address=" + self.address
			data += '\n'
			data += "unit=" + self.unit
			data += '\n'
			data += "command=" + self.command
			data += '\n'
		elif self.type == "zwave.basic"
			data += "node=" + self.device
			data += '\n'
			data += "command=" + self.command
			data += '\n'
		data += '}'
		return data
	def getData(self):
		d = self.generate_header()
		d += self.generate_data()
		return d

x = XPL("dqsd", "abc")
x.x10security("on", "ds")
print x.getData()