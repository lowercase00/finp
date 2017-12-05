from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv

def export_ledger():

    cnx = mariadb.connect(user='root', password='', database='base_teste')
    cursor = cnx.cursor()

    query = """
            SELECT ID, data, credito, debito, descricao, valor
            FROM ledger_teste
            ORDER BY id DESC
            """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    desc = cursor.description
    cnx.close()
    
    ledger_completo = [dict(itertools.izip([col[0] for col in desc], row)) 
        for row in rows]

    return rows

print export_ledger()