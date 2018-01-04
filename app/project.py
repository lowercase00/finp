# -*- coding: latin-1 -*-

## We can use this to work on the project
# THis is what I have to far, you can run this code to see how the DataFrame is organized

from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import pandas as pd
import numpy as np
from collections import defaultdict


def make_is_report():

    cnx = mariadb.connect(  user='root',
                            password='',
                            database='db_finp'
                            )

    cursor = cnx.cursor()

    # This query gets the "stacked" version of the Income Statement (IS).
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

    # IS to a dataframe (right so it can be joined with the accounts dataframe ahead)
    right           = pd.read_sql(query, cnx)
    right['data']   = pd.to_datetime(right['data'], format='%m-%y')


    # This query is to get the full hierarchical tree of the Chart of Accounts
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

    # Full tree saved into a dataframe
    left        = pd.read_sql(query, cnx)


    # The join of the tree (left) and the pivoted income statement
    report_is   = pd.merge(left, right)

    # This is the Income Statement in it's regular form - all 4 level of accounts on the left side, dates on the columns
    report_is   = pd.pivot_table(report_is, values='Value', index=['Level1', 'Level2', 'Level3', 'Level4'], columns=['data'])
    report_is   = report_is.fillna(0)

    # Grouped sum of the Level 1 accounts
    l1_sum      = report_is.groupby(level=[0]).sum()
    l1_sum      = l1_sum.transpose()
    l1_sum      = l1_sum.round(2)
    l1_sum      = l1_sum.to_dict()
    
    # Grouped sum of the Level 2 accounts
    l2_sum      = report_is.groupby(level=[1]).sum()
    l2_sum      = l2_sum.transpose()
    l2_sum      = l2_sum.round(2)
    l2_sum      = l2_sum.to_dict()
    
    # Grouped sum of the Level 3 accounts
    l3_sum      = report_is.groupby(level=[2]).sum()
    l3_sum      = l3_sum.round(2)
    l3_sum      = l3_sum.transpose()
    l3_sum      = l3_sum.to_dict()

    # Grouped sum of the Level 4 accounts
    l4_sum      = pd.pivot_table(right, values='Value', index='data', columns='Level4')
    l4_sum      = l4_sum.fillna(0)
    l4_sum      = l4_sum.round(2)
    l4_sum      = l4_sum.to_dict()


    # Rendering the Income Statement to HTML so help visualization
    dataset     = report_is.to_html()
    return render_template('project1.html', isdata=dataset)

