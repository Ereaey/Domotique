import time
sys.path.append("../Server")
from xpl_sender import *
from xpl import *

c = XPL_Sender(5000)
data = XPL_Msg("time", "*")

while True:
	data.resetBody()
	data.datetime(str(time.time()), str(time.time()), str(time.time()))
	c.send(data.getData())
	time.sleep(60)

