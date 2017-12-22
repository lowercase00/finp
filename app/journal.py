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
            SELECT CAST(ROUND(id,2) AS CHAR(10)), DATE_FORMAT(date_cash, '%b-%y'), credit, debit, CAST(ROUND(value,2) AS CHAR(10)) FROM journal
            ORDER BY ID ASC
            """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    desc = cursor.description
    cnx.close()
    
    journal = [list(i) for i in rows]
    journal = [[s.encode('ascii', 'ignore') for s in i] for i in journal]


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



