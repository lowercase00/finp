import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv, json, jsonify, collections, itertools

def export_data():
    
    cnx = mariadb.connect(user='root', password='', database='base_completa')
    cursor = cnx.cursor()
    
    chart_of_accounts = """
                        SELECT nivel4
                        FROM pdc
                        WHERE nivel0 = 'balance_sheet'
                        """
    

    cursor.execute(chart_of_accounts)
    accounts = cursor.fetchall()
    
    cnx.close()
    
    for account in accounts:
        
        cnx = mariadb.connect(user='root', password='', database='base_completa')
        cursor = cnx.cursor()
        
        print "2. Conecting..."

        query = """
                SELECT Y, M,(@total := @total + Fluxo) AS ValorTotal
                FROM (
                SELECT year(data) AS Y, month(data) AS M, 
                        (
                            SUM(IF(Credito="%s", valor, 0))-
                            SUM(IF(Debito="%s", valor, 0))
                        ) AS Fluxo
                    FROM ledger
                    GROUP BY YEAR(DATA), MONTH(DATA)
                    ) AS T,
                (SELECT @total:=0) AS n;
                """ % account, account
        print "3. Query written"

        cursor.execute(query)
        rows = cursor.fetchall()        
        cnx.commit()

        print account
        print json.dumps(rows)


    return lista

results = export_data()