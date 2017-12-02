from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg




# Estabilishes a connection to the ledger



# Get form input and saves it to ledger
#
@app.route('/put_data', methods=['GET', 'POST'])
def put_data():
    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )
    cursor = cnx.cursor()
    
    add_reg =   """
                INSERT INTO ledger_teste
                (data, credito, debito, descricao, valor)
                VALUES (%s, %s, %s, %s, %s)
                """
	
    data = request.form['data']
    cred = request.form['credito']
    deb = request.form['debito']
    desc = request.form['descricao']
    valor = request.form['valor']


    registro = (data, cred, deb, desc, valor)

    cursor.execute(add_reg, registro)
    cnx.commit()

    return redirect(url_for('ledger'))





# Export ledger and arranges data in JSON format to be shown on data grid
#
@app.route('/export_ledger', methods=['GET', 'POST'])
def export_ledger():
    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )
    cursor = cnx.cursor()

    query = """
            SELECT ID, data, credito, debito, descricao, valor
            FROM ledger_teste
            ORDER BY data DESC
            """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    desc = cursor.description
    cnx.close()
    
    ledger_completo = [dict(itertools.izip([col[0] for col in desc], row)) 
        for row in rows]

    return json.dumps(ledger_completo)    