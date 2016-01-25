import socket
import sys

class XPL_Sender:
	def __init__(self, port):
		self.port = port
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
	def send(self, data):
		try:
			self.s.sendto(data, ("<broadcast>", self.port))
			#self.s.sendto(data, ("", self.port))
		except:
			pass

	def close(self):
		self.s.close()

if __name__ == '__main__':
	c = XPL_Sender(int(sys.argv[1]))
	c.send(sys.argv[2])