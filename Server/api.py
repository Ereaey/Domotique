from bottle import Bottle, run
import sqlite3
import json

app = Bottle()

@app.route('/login/:login/:password')
def connection(login, password):
    return "Login : " + login + " Password : " + password

@app.route('/bridges/:key')
def bridges(key):
    return "bridges"

@app.route('/actuators/:key')
def addsqd(key):
	return json.dumps({"c" : 0, "d" : 1})

@app.route('/sensors/:key')
def sensors(key):
	return "salut les gens"

@app.route('/dqsd/')
def sqd():
	return "qdsqd"


run(app, host='localhost', port=8080, reloader=True)