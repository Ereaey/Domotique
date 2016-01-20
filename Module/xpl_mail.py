import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import sys
import socket
sys.path.append("../Server")
from xpl_parser import *


class Mail:
	def __init__(self, login, password):
		self.login = login
		self.server = smtplib.SMTP("smtp.gmail.com", 587)
		self.server.starttls()
		self.server.login(self.login, password)

	def send(self, to, subject, body):
		self.msg = MIMEMultipart()

		self.msg['From'] = self.login
		self.msg['To'] = to
		self.msg['Subject'] = subject

		self.msg.attach(MIMEText(body, 'plain'))

		self.server.sendmail(self.login, to, self.msg.as_string())

	def close(self):
		self.server.quit()

if __name__ == '__main__':
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind(('', 5001))
	except:
		print "Error socket"
	mail = Mail("domotique.project@gmail.com", "Aze12345")
	while (1):
		d = s.recvfrom(1024)
		e = XPL_Parser(d[0])
		if e.extractProtocol() == "sendmsg.smtp":
			mail.send(e.extract("to"), e.extract("subject"), e.extract("body"))
		print "Mail sent"