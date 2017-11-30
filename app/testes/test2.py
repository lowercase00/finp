import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv, json, jsonify, collections, itertools

def export_data():
    cnx = mariadb.connect(user='root', password='', database='base_completa')
    cursor = cnx.cursor()

    query = """
            SELECT Y, M,(@total := @total + Fluxo) AS ValorTotal
            FROM (
            SELECT year(data) AS Y, month(data) AS M, 
                    (
                        SUM(IF(Credito='Conta Corrente Itau', valor, 0))-
                        SUM(IF(Debito='Conta Corrente Itau', valor, 0))
                    ) AS Fluxo
                FROM ledger
                GROUP BY YEAR(DATA), MONTH(DATA)
                ) AS T,
            (SELECT @total:=0) AS n;
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    desc = cursor.description
    cnx.close()
    
    
    lista = [dict(itertools.izip([col[0] for col in desc], row)) 
        for row in rows]

    return lista

results = export_data()

with open('base_conta1.json', 'wb+') as fp:
    json.dump(results, fp)

print results