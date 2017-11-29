import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv, json, jsonify, collections, itertools
import pandas as pd

def export_data():

    cnx = mariadb.connect(user='root', password='', database='base_completa')
    cursor = cnx.cursor()
    print "1. Conecting..."

    chart_of_accounts = [
                        "Conta Corrente Itau",
                        "Cartao Itau Master",
                        "Cartao Itau VISA",
                        "Carteira"
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

        df=pd.read_sql_query(query, account)
        print "4. Query executed"

        print df


    return lista

results = export_data()

# with open('base_conta222.json', 'wb+') as fp:
#     json.dump(results, fp)

