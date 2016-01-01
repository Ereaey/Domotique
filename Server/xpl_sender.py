import socket
import sys

class XPL_Sender:
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

	def send(self, data):
		try:
			self.s.connect((self.ip, self.port))
			self.s.send(data)
			print("Message send")
		except:
			pass

	def close(self):
		self.s.close()

if __name__ == '__main__':
	c = XPL_Sender(sys.argv[1], int(sys.argv[2]))
	c.send(sys.argv[3])