from app import app
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,session
from configuraciones import *

import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()


@app.route('/')
def home():

	sql ="""
	select rut from alumnos
	"""
	 
	cur.execute(sql)
	user  = cur.fetchall()

	sql ="""
	select rut from empleados
	"""
	
	cur.execute(sql)
	user_empl  = cur.fetchall()

	if not session.get('logged_in'):
		return render_template('login.html')
    
	for e in user_empl:
		if request.form['username'] == e[0]:
			return redirect(url_for('index2'))

	for u in user:
		if request.form['username'] == u[0]:
			return redirect(url_for('index'))

    
@app.route('/login', methods=['POST'])
def do_admin_login():

	sql ="""
	select rut from alumnos
	"""
	print sql 
	cur.execute(sql)
	user  = cur.fetchall()

	sql ="""
	select rut from empleados
	"""
	 
	cur.execute(sql)
	user_empl  = cur.fetchall()

	

	for e in user_empl:
		if request.form['username'] == e[0]:
			session['logged_in'] = True
			session['user_empl'] = e[0]
		else:
			flash('wrong password!')

	for u in user:
		if request.form['username'] == u[0]:
			session['logged_in'] = True
			session['user'] = u[0]
		else:
			flash('wrong password!')

	

	
	return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()



"""pagina de inicio"""

@app.route('/index')
def index():

	user = session.get('user')

	sql ="""
	select nombre from alumnos where rut = '%s'
	"""%(user)
	
	cur.execute(sql)
	user2  = cur.fetchall()
	

	return render_template("index.html",user2=user2)

@app.route('/index2')
def index2():

	user_empl = session.get('user_empl')

	sql ="""
	select nombre from empleados where rut = '%s'
	"""%(user_empl)
	
	cur.execute(sql)
	user  = cur.fetchall()
	

	return render_template("index2.html",user=user)

@app.route('/ui')
def ui():

	return render_template("ui.html")

@app.route('/tabla')
def tabla():

	sql ="""
	select * from alumnos
	"""
	
	cur.execute(sql)
	alumnos  = cur.fetchall()

	return render_template("tabla.html",alumnos=alumnos)

@app.route('/aggalumno', methods=['GET', 'POST'])
def aggalumno():

	if request.method == 'POST':
		rut =  request.form['rut']
		nombre =  request.form['nombre']
		edad =  request.form['edad']
		correo =  request.form['correo']
		cod_curso =  request.form['cod_curso']
		rut_apod =  request.form['rut_apod']
	
		sql = """ insert into alumnos  
		(rut,nombre,edad,correo,cod_curso,rut_apod) 
		values ('%s','%s',%s,'%s','%s','%s' ) """%(rut,nombre,edad,correo,cod_curso,rut_apod)
		cur.execute(sql)
		conn.commit()

	return render_template("aggalumno.html")

@app.route('/borrar', methods=['GET', 'POST'])
def borrar():


	if request.method == 'POST':
		rut =  request.form['rut']
		
		sql = """ delete from alumnos where rut = '%s' """%(rut)
		cur.execute(sql)
		conn.commit()

	return render_template("borrar.html")

@app.route('/update', methods=['GET', 'POST'])
def update():


	if request.method == 'POST':
		rut =  request.form['rut']
		
		sql = """ delete from alumnos where rut = '%s' """%(rut)
		cur.execute(sql)
		conn.commit()



	return render_template("update.html")



