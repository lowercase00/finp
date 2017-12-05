from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import views




# class LedgerConnection():

##################### EXPORT LEDGER #####################

@app.route('/_export_ledger', methods=['GET', 'POST'])
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






##################### INPUT IN LEDGER #####################

@app.route('/_journal_entry', methods=['GET', 'POST'])
def journal_entry():
    
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
    cnx.close()

    return redirect(url_for('ledger'))








##################### EDIT ENTRIES #####################

@app.route('/_edit_ledger', methods=['GET', 'POST'])
def edit_ledger():    

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )
    cursor = cnx.cursor()









###################### DELETE ENTRIES #####################

@app.route('/_delete_ledger', methods=['GET', 'POST'])
def delete_ledger():

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )
    cursor = cnx.cursor()



