import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

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

e = Mail("anthony.arthus@gmail.com", "arthus1204")
e.send("baudelotmarvin@gmail.com", "Test", "dqsd")
e.close()
