from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg

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