from app import app
from flask import render_template, request
import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv
import mysql.connector as mariadb
import json
import jsonify
import collections
import itertools


@app.route('/put_data', methods=['GET', 'POST'])
def put_data():
    cnx = mariadb.connect(user='root', password='', database='test')
    cursor = cnx.cursor()
    add_reg = ("INSERT INTO base_teste "
	   	   "(data, cred, deb, dsc, valor) "
	       "VALUES (%s, %s, %s, %s, %s)")
	
    data = request.form['data']
    cred = request.form['cred']
    deb = request.form['deb']
    dsc = request.form['dsc']
    valor = request.form['valor']

    registro = (data, cred, deb, dsc, valor)

    cursor.execute(add_reg, registro)
    cnx.commit()

    return redirect(url_for('ledger'))


@app.route('/export_data', methods=['GET', 'POST'])
def export_data():
    cnx = mariadb.connect(user='root', password='', database='test')
    cursor = cnx.cursor()

    query = "SELECT ID, data, cred, deb, dsc, valor FROM base_teste"
    
    cursor.execute(query)
    rows = cursor.fetchall()
    desc = cursor.description
    cnx.close()
    
    
    lista = [dict(itertools.izip([col[0] for col in desc], row)) 
        for row in rows]

    return lista    
    # return json.dumps(lista)
