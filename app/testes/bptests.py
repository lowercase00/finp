import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv, json, jsonify, collections, itertools

def export_data_bs():

    cnx = mariadb.connect(user='root', password='', database='base_completa')
    cursor = cnx.cursor()
    print "1. Conecting..."

    chart_of_accounts = [
                        'Conta Corrente Itau',
                        'Cartao Itau Master',
                        'Cartao Itau VISA',
                        'Carteira'
                        ]

    for account in chart_of_accounts:
        print "2. Loop begins"

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
                """
        print "3. Query written"

        cursor.execute(query, account)
        print "4. Query executed"

        rows = cursor.fetchall()
        print "5. Fetchall"

        desc = cursor.description
        print "6. Cursor description"
    
        lista = [dict(itertools.izip([col[0] for col in desc], row)) 
            for row in rows]
        
        cnx.commit()

        print account
        print json.dumps(lista)

    return lista

results = export_data_bs()

# with open('base_conta222.json', 'wb+') as fp:
#     json.dump(results, fp)

