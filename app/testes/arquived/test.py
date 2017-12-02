from flask import render_template, request
import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv
import mysql.connector as mariadb
import json
import jsonify
import collections
import itertools

# cnx = mariadb.connect(user='root', password='', database='test')
# cursor = cnx.cursor()

# query = "SELECT ID, data, cred, deb, dsc, valor FROM base_teste"

# cursor.execute(query)
# rows = cursor.fetchall()
# results = json.dumps(rows)
# print results


def export_data():
    cnx = mariadb.connect(user='root', password='', database='base_completa')
    cursor = cnx.cursor()

    query = "SELECT DataCaixa, Credito, Debito, valor FROM ledger WHERE Credito='Conta Corrente Itau'"
    
    cursor.execute(query)
    rows = cursor.fetchall()
    desc = cursor.description
    cnx.close()
    
    
    lista = [dict(itertools.izip([col[0] for col in desc], row)) 
        for row in rows]

    return lista

results = export_data()

with open('datateste.json', 'wb+') as fp:
    json.dump(results, fp)

print results