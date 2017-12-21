# views.py

from flask import render_template, jsonify
from app import app
import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv, json, collections, itertools
import config as cfg
from random import sample

#Returns { "Salario" : [ [2015,4,10], [ 2016,4,10].... ]}
#Returns { "Salario" : [ [10.000], [12.000].... ]}
def data_test():

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )

    cursor = cnx.cursor()

    # account = "Salario"
    # table = "ledger_teste"
    # params = (account, account, table)

    query = """
            SELECT
                (
                    SUM(IF(Credito="Salario", valor, 0))-
                    SUM(IF(Debito="Salario", valor, 0))
                )
            AS Fluxo    
            FROM ledger_teste
            GROUP BY YEAR(data), MONTH(data)
            """ #% (params)
    
    
    cursor.execute(query)
    query_time_series = cursor.fetchall()

    results = jsonify({'Salario' : query_time_series})
    cnx.close()
 
    print query_time_series
    return results


# Returns JSON with names
"""
[{
    "year(data)": 2015,
    "month(data)": 4,
    "Fluxo": 0.0
}, {
    "year(data)": 2015,
    "month(data)": 5,
    "Fluxo": 10000.0
}, {
"""

def TestFetch():
    
    cnx = mariadb.connect(user='root', password='', database='base_teste')
    cursor = cnx.cursor()

    query = """
        SELECT 
            (
                SUM(IF(Credito="Salario", valor, 0))-
                SUM(IF(Debito="Salario", valor, 0))
            )
        AS Salario    
        FROM ledger_teste
        GROUP BY YEAR(data), MONTH(data)
        """

    cursor.execute(query)
    rows = cursor.fetchall()
        
    desc = cursor.description
    
    lista = [dict(itertools.izip([col[0] for col in desc], row)) 
        for row in rows]

    salario = list(rows)
    cnx.close()

    return json.dumps(salario)


def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None