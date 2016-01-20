import time
import sys
sys.path.append("../Server")
from xpl_sender import *
from xpl import *

c = XPL_Sender(5000)
data = XPL_Msg("time", "*")

print "Demarrage module clock"

while True:
	try:
		data.resetBody()
		data.datetime(str(time.time()), str(time.time()), str(time.time()))
		c.send(data.getData())
		print "Temps envoyee"
		time.sleep(60)
	except KeyboardInterrupt:
		print "Fermeture module clock"
		sys.exit(0)

