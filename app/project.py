# -*- coding: latin-1 -*-

## We can use this to work on the project
# THis is what I have to far, you can run this code to see how the DataFrame is organized

# from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
# import config as cfg
import pandas as pd
import numpy as np


def make_is_report():

    cnx = mariadb.connect(  user='root',
                            password='',
                            database='db_finp'
                            )

    cursor = cnx.cursor()

    query = """
            SELECT date_format(date_cash, '%m-%y') as data, conta as Level4, ROUND(sum(valor), 2) as Value, parent, account, code
                FROM (
                    SELECT parent, code, act_debit.report AS report, date_cash, debit AS conta, account, SUM(CASE WHEN act_debit.nature = 0 THEN value ELSE -value END) AS valor 
                    FROM journal 
                    RIGHT JOIN accounts AS act_debit ON act_debit.account = journal.debit
                    GROUP BY debit, YEAR(date_cash), MONTH(date_cash)
                UNION
                    SELECT parent, code, act_credit.report AS report, date_cash, credit AS conta, account, SUM(CASE WHEN act_credit.nature = 0 THEN value ELSE -value END) AS valor
                    FROM journal
                    RIGHT JOIN accounts AS act_credit ON act_credit.account = journal.credit
                    GROUP BY credit, YEAR(date_cash), MONTH(date_cash)
                ) AS aliastabela
            WHERE (report="Income Statement")
            GROUP BY conta, YEAR(date_cash), MONTH(date_cash)
            ORDER BY date_cash ASC
            """

    right          = pd.read_sql(query, cnx)
    right['data']  = pd.to_datetime(right['data'], format='%m-%y')


    accounts = "accounts"
    params = (accounts, accounts, accounts, accounts)
    
    cursor = cnx.cursor()

    query = """
            SELECT
            t1.account AS Level1,
            t2.account AS Level2,
            t3.account AS Level3,
            t4.account AS Level4

            FROM %s AS t1

            LEFT JOIN %s AS t2 ON t2.parent = t1.code
            LEFT JOIN %s AS t3 ON t3.parent = t2.code
            LEFT JOIN %s AS t4 ON t4.parent = t3.code

            WHERE      
            t1.account = 'Receitas' OR
            t1.account = 'Despesas' OR
            t1.account = 'Nao Operacionais';
            """ % (params)

    left        = pd.read_sql(query, cnx)

    report_is   = pd.merge(left, right)
    report_is   = pd.pivot_table(report_is, values='Value', index=['Level1', 'Level2', 'Level3', 'Level4'], columns=['data'])
    report_is   = report_is.fillna(0)

    dataset     = report_is.to_html()

    return render_template('project1.html', isdata=dataset)



def GetISLevel():

    cnx = mariadb.connect(  user='root',
                            password='',
                            database='db_finp'
                            )

    cursor = cnx.cursor()

    level1 =    """
                SELECT code, account, parent
                FROM accounts
                WHERE level = 1
                AND report = "Income Statement"
                """

    cursor.execute(level1)
    rows = cursor.fetchall()
    desc = cursor.description
    is_l1_accounts = [dict(itertools.izip([col[0] for col in desc], row)) for row in rows]

    level2 =    """
                SELECT code, account, parent
                FROM accounts
                WHERE level = 2
                AND report = "Income Statement"
                """

    cursor.execute(level2)
    rows = cursor.fetchall()
    desc = cursor.description
    is_l2_accounts = [dict(itertools.izip([col[0] for col in desc], row)) for row in rows]

    level3 =    """
                SELECT code, account, parent
                FROM accounts
                WHERE level = 3
                AND report = "Income Statement"
                """

    cursor.execute(level3)
    rows = cursor.fetchall()
    desc = cursor.description
    is_l3_accounts = [dict(itertools.izip([col[0] for col in desc], row)) for row in rows]

    level4 =    """
                SELECT code, account, parent
                FROM accounts
                WHERE level = 4
                AND report = "Income Statement"
                """

    cursor.execute(level4)
    rows = cursor.fetchall()
    desc = cursor.description
    is_l4_accounts = [dict(itertools.izip([col[0] for col in desc], row)) for row in rows]

    chart = is_l4_accounts + is_l3_accounts + is_l2_accounts + is_l1_accounts
    chart = json.dumps(chart)