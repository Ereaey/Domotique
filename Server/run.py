import os
import subprocess
import sys
import time

print "Demarrage"
main = subprocess.Popen(['python', 'main.py', '>>', 'log_s.txt'])
api = subprocess.Popen(['python3', 'api.py'])
#modules = subprocess.Popen(['python', '../Module/main.py', '>>', 'log_mod.txt'])

while(1):
	try:
		time.sleep(60)
		print "Module en cours d'execution"
	except KeyboardInterrupt:
		print "Fermeture"
		main.terminate()
		api.terminate()
		#modules.terminate()
		time.sleep(2)
		sys.exit(0)
