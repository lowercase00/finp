from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import views
import datetime




##################### EXPORT JOURNAL #####################

def export_journal():
    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseprod']
                            )
    cursor = cnx.cursor()

    query = """
            SELECT ID, date_cash, credit, debit, description, value
            FROM journal
            ORDER BY date_cash DESC
            LIMIT 50
            """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    desc = cursor.description
    cnx.close()
    
    journal = [list(i) for i in rows]


    journal = [ ['data 1', 'credito 1', 'item 1'],
                ['data 2', 'credito 2', 'item 2'],
                ['data 3', 'credito 3', 'item 3'],
                ['data 4', 'credito 4', 'item 4'],
                ['data 5', 'credito 5', 'item 5']]

    return render_template('journal.html', journal=journal)







##################### INPUT IN LEDGER #####################

def journal_entry():
    
    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseprod']
                            )
    cursor = cnx.cursor()
    
    add_reg =   """
                INSERT INTO journal
                (date_cash, credit, debit, description, value)
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








# ##################### EDIT ENTRIES #####################

# def edit_ledger():    

#     cnx = mariadb.connect(  user=cfg.db['user'],
#                             password=cfg.db['pwd'],
#                             database=cfg.db['baseteste']
#                             )
#     cursor = cnx.cursor()









# ###################### DELETE ENTRIES #####################

# def delete_ledger():

#     cnx = mariadb.connect(  user=cfg.db['user'],
#                             password=cfg.db['pwd'],
#                             database=cfg.db['baseteste']
#                             )
#     cursor = cnx.cursor()



