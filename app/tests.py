from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import views
import datetime




################################## EXPORT JOURNAL ##################################

def test_function():
    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseprod']
                            )
    cursor = cnx.cursor()

    query = """
            SELECT CAST(ROUND(id,2) AS CHAR(10)),
            DATE_FORMAT(date_cash, '%b-%y'), credit, debit, CAST(ROUND(value,2) AS CHAR(10))
            FROM journal
            ORDER BY ID ASC
            """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    desc = cursor.description
    cnx.close()
    
    journal = [list(i) for i in rows]
    journal = [[s.encode('ascii', 'ignore') for s in i] for i in journal]

    testlist = [    ["linha 1", "linha 1", "linha 1", "linha 1"],
                    ["linha 2", "linha 1", "linha 1", "linha 1"],
                    ["linha 3", "linha 1", "linha 1", "linha 1"],
                    ["linha 4", "linha 1", "linha 1", "linha 1"],
                    ["linha 5", "linha 1", "linha 1", "linha 1"],
                    ["linha 6", "linha 1", "linha 1", "linha 1"],
                    ["linha 7", "linha 1", "linha 1", "linha 1"],
                    ["linha 8", "linha 1", "linha 1", "linha 1"]]

    return render_template('tests.html', testlist=testlist)





