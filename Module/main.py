import os
import subprocess
import sys
import time

print "Module Ping, Mail, Clock"
ping = subprocess.Popen(['python', 'xpl_ping.py'])
mail = subprocess.Popen(['python', 'xpl_mail.py'])
clock = subprocess.Popen(['python', 'xpl_clock.py'])
sys.stdout.flush()

while(1):
	try:
		time.sleep(60)
		print "Module en cours d'execution"
		sys.stdout.flush()
	except KeyboardInterrupt:
		print "Fermeture des modules"
		ping.terminate()
		mail.terminate()
		clock.terminate()
		time.sleep(2)
		sys.stdout.flush()
		sys.exit(0)