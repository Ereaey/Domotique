import time
import os
import sys
sys.path.append("../Server")
from xpl_sender import *
from xpl import *

c = XPL_Sender(5000)
data = XPL_Msg("ping", "*")

while True:
	hostname = "google.com"
	response = os.popen('ping -c 1 ' + hostname).read()

	f = response.find('time=', 0)
	e = response.find(' ', f)

	data.resetBody()
	data.ping(response[f + 5:e])
	c.send(data.getData())
	time.sleep(60)