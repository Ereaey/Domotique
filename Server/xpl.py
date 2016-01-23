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
	def datetime(self, datetime, date, time):
		self.type = "datetime.basic"
		self.add("datetime", datetime)
		self.add("date", date)
		self.add("time", time)
	def dawndusk(self, type, status):
		self.type = "dawndusk.basic"
		self.add("type", type)
		self.add("status", status)
	def mail(self, to, subject, body):
		self.type = "sendmsg.smtp"
		self.add("to", to)
		self.add("subject", subject)
		self.add("body", body)
	def screen(self, command):
		self.type = "osd.basic"
		self.add("command", command)
	def screenWrite(self, text):
		self.type = "osd.basic"
		self.add("command", "write")
		self.add("text", text)
	def x10(self, device, command):
		self.type = "x10.basic"
		self.add("device", device)
		self.add("command", command)
	def sensor(self, device, type, current):
		self.type = "sensor.basic"
		self.add("device", device)
		self.add("type", type)
		self.add("current", current)		
	def x10security(self, device, command):
		self.type = "x10.security"
		self.add("device", device)
		self.add("command", command)
	def xpl(self, device, command):
		self.type = "xpl.basic"
		self.add("device", device)
		self.add("command", command)
	def zwave(self, device, command):
		self.type = "zwave.basic"
		self.add("node", device)
		self.add("command", command)
	def ping(self, ping):
		self.type = "ping.basic"
		self.add("ping", ping)
	def resetBody(self):
		self.body = ""
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
	x.sensor("A3", "input", "pulse")
	print x.getData()