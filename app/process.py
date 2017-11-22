from app import app
from flask import render_template, request
import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv


#Conecta base de dados e cria o cursor
cnx = mariadb.connect(user='root', password='', database='test')
cursor = cnx.cursor()

#decorator que puxa informacoes e manda para a base
@app.route('/process', methods=['GET', 'POST'])
def process():
	print "1. it is processing..."
	add_reg = ("INSERT INTO base "
	   	   "(data, cred, deb, dsc, valor) "
	       "VALUES (%s, %s, %s, %s, %s)")
	print "2. query feita..."

	data = request.form['data']
	print "3. data coletada..."

	cred = request.form['cred']
	print "4. cred coletada..."

	deb = request.form['deb']
	print "5. deb coletada..."
	
	dsc = request.form['dsc']
	print "6. dsc coletada..."
	
	valor = request.form['valor']
	print "7. valor coletada..."
	
	print "8. todos os dados coletados!"
	registro = (data, cred, deb, dsc, valor)

	print "9. executando..."
	cursor.execute(add_reg, registro)
	cnx.commit()
	print "10. salvo na base de dados!"

	ult_reg = cursor.lastrowid

	cursor.close()
	cnx.close()

	return redirect(url_for('ledger'))



# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
	
# 	print "1. it is processing CSV file..."
# 	file = request.files['file']

# 	csv_data = csv.reader(file('file'))
# 	print "2. It is CSV..."

# 	for row in csv_data:
# 		print "3. iterando linhas..."
	
# 	    add_file = ("INSERT INTO base "
#                     "(data, cred, deb, dsc, valor) "
#                     "VALUES (%s, %s, %s, %s, %s), row")
#         extraidos = (data, cred, deb, dsc, valor)

#     cursor.execute(add_file, extraidos)
# 	print "4. cursor executado..."
	    
# 	cnx.commit()
# 	print "5. commit de dados..."

# 	cursor.close()
# 	cnx.close()
	
# 	print "6. finalizado!"
#     return redirect(url_for('ledger'))