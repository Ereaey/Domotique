from bottle import Bottle, run
import sqlite3
import json
import psutil

app = Bottle()

@app.route('/login/:login/:password')
def connection(login, password):
	coon = sqlite3.connect('domotique.sqlite')
	c = coon.cursor()
	c.execute("""SELECT * FROM users WHERE login=? and password=?""", (login, password, ))
	row = c.fetchone()
	if row is None:
		data = json.dumps({"success" : False})
	else:
		data = json.dumps({"success" : True, "id" : row[0], "login": row[1]})
	return data

@app.route('/rooms')
def rooms():
	coon = sqlite3.connect('domotique.sqlite')
	c = coon.cursor()
	c.execute("""SELECT * FROM rooms""")
	rows = c.fetchall()
	data = []
	for row in rows:
		data.append({"id" : row[0], "name": row[1]})
	return json.dumps({"rooms" : data})

@app.route('/equipments_type')
def types():
	coon = sqlite3.connect('domotique.sqlite')
	c = coon.cursor()
	c.execute("""SELECT * FROM equipments_type""")
	rows = c.fetchall()
	data = []
	for row in rows:
		data.append({"id" : row[0], "name": row[1], "path_image": row[2]})
	return json.dumps({"equipments_type" : data})

@app.route('/room/:id')
def room(id):
	coon = sqlite3.connect('domotique.sqlite')
	c = coon.cursor()
	c.execute("""SELECT * FROM equipments WHERE id_room=?""", (id, ))
	rows = c.fetchall()
	data = []
	for row in rows:
		data.append({"id" : row[0], "name": row[4]})
	return json.dumps({"room" : data})

@app.route('/equipments')
def equipments():
	coon = sqlite3.connect('domotique.sqlite')
	c = coon.cursor()
	c.execute("""SELECT * FROM equipments""")
	rows = c.fetchall()
	data = []
	for row in rows:
		data.append({"id" : row[0], "name": row[4]})
	return json.dumps({"equipments" : data})

@app.route('/addEquipment/:id_type/:id_protocol/:id_room/:name/:data1/:data2/:data3/:unit')
def addEquipment(id_type, id_protocol, id_room, name, data1, data2, data3, unit):
	coon = sqlite3.connect('domotique.sqlite')
	c = coon.cursor()
	c.execute("INSERT INTO equipments(id_type, id_room, id_protocol, name, data1, data2, data3, unit) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (id_type, id_room, id_protocol, name, data1, data2, data3, unit))
	coon.commit()
	return json.dumps({"success" : True})

@app.route('/protocols')
def protocoles():
	coon = sqlite3.connect('domotique.sqlite')
	c = coon.cursor()
	c.execute("""SELECT * FROM protocols""")
	rows = c.fetchall()
	data = []
	for row in rows:
		data.append({"id" : row[0], "name": row[1], "description" : row[2]})
	return json.dumps({"protocols" : data})

@app.route('/')
def api():
	data = "<center><h1>Api du projet domotique</h1></center><br />"
	data += "/login/:login/:password<br/>"
	data += "/rooms<br />"
	data += "/room/:id<br />"
	data += "/equipments_type<br />"
	data += "/addEquipment/:id_type/:id_protocol/:id_room/:name/:data1/:data2/:data3/:value/:unit<br />"
	data += "/protocols<br />"
	data += "/log<br />"
	data += "/stats<br />"
	return data

@app.route('/log_udp')
def log():
	file = open("log.txt", "r")
	data = ""
	for line in file:
		data += line
		data += '<br />'
	file.close()
	return data

@app.route('/log_server')
def log():
	file = open("log_s.txt", "r")
	data = ""
	for line in file:
		data += line
		data += '<br />'
	file.close()
	return data


@app.route('/stats')
def stats():
	data = "Boot time : "
	data += str(psutil.boot_time())
	data += '<br />'
	data += "Memory : "
	data += str(psutil.virtual_memory()[1])
	data += " / "
	data += str(psutil.virtual_memory()[0])
	data += '<br />'
	data += "CPU : "
	data += str(psutil.cpu_percent(interval=1, percpu=True))
	return data

run(app, host='localhost', port=8080)