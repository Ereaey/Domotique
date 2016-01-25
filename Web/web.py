import bottle
import sqlite3
import json
import psutil
from bottle import static_file
from urllib.request import urlopen

ip = "localhost:8080"
@bottle.route('/')
@bottle.view("index.tpl")
def index():
	data = urlopen("http://" + ip + "/rooms")
	e = json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))
	data.close()

	data = urlopen("http://" + ip + "/equipments")
	f = json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))
	data.close()

	return {"title":"Domotique","menu": e["rooms"], "equipments" : f["equipments"]}

@bottle.route('/room/:id')
@bottle.view("index.tpl")
def room(id):
	data = urlopen("http://" + ip + "/rooms")
	e = json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))
	data.close()

	data = urlopen("http://" + ip + "/room/" + str(id))
	f = json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))
	data.close()
	return {"title":"Domotique","menu": e["rooms"], "equipments" : f["room"]}

@bottle.route('/equipment/:id')
def equipment(id):
	data = urlopen("http://" + ip + "/rooms")
	e = json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))
	data.close()

	data = urlopen("http://" + ip + "/equipments")
	f = json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))
	data.close()
	return {"title":"Domotique","menu": e["rooms"], "equipments" : f["room"]}

@bottle.route('/log')
@bottle.view("console.tpl")
def log():
	data = urlopen("http://" + ip + "/rooms")
	e = json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))
	data.close()

	data = urlopen("http://" + ip + "/log_udp")
	f = data.read().decode(data.info().get_param('charset') or 'utf-8')
	data.close()
	g = str(f)
	#g = g.replace("<br />", '\n\r')
	return {"title":"Log UDP", "menu": e["rooms"], "log" : g}

@bottle.route('/log_server')
@bottle.view("console.tpl")
def log():
	data = urlopen("http://" + ip + "/rooms")
	e = json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))
	data.close()

	data = urlopen("http://" + ip + "/log_server")
	f = data.read().decode(data.info().get_param('charset') or 'utf-8')
	data.close()
	g = str(f)
	#g = g.replace("<br />", '\n\r')
	return {"title":"Log Serveur", "menu": e["rooms"], "log" : g}

@bottle.route('/log_module')
@bottle.view("console.tpl")
def log():
	data = urlopen("http://" + ip + "/rooms")
	e = json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))
	data.close()

	data = urlopen("http://" + ip + "/log_module")
	f = data.read().decode(data.info().get_param('charset') or 'utf-8')
	data.close()
	g = str(f)
	#g = g.replace("<br />", '\n\r')
	return {"title":"Log Modules", "menu": e["rooms"], "log" : g}

@bottle.route('/static/<path:path>')
def static(path):
	return static_file(path, root='')



bottle.run(bottle.app(), host='localhost', port=8085, reloader=True)