import nxppy
import time
import xpl
import xpl_sender
import sqlite3


mifare=nxppy.Mifare()

conn = XPL_Sender(5000)

print "NFC : Open, PORT : 5000"
while True:
	try:
		uid = mifare.select()
		print "Read uid", uid
		
		if uid == "FA5958EA":#Thibault
			message = XPL("NFC", "*")
			message.sensor("A3", "input", "pulse")
			conn.send(message.getData())
			time.sleep(30)
		elif uid == "76F11908":#Adeline
			message = XPL("NFC", "*")
			message.sensor("A4", "input", "pulse")
			conn.send(message.getData())
			time.sleep(30)
		elif uid == "DA0D57EA":#Anthony
			message = XPL("NFC", "*")
			message.sensor("A5", "input", "pulse")
			conn.send(message.getData())
			time.sleep(30)					
		time.sleep(3)
	except nxppy.SelectError:
		pass
	except (KeyboardInterrupt, SystemExit):
		print "NFC : Close"