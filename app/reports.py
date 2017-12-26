from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import views
import pandas as pd




################################## EXPORT BALANCE SHEET ACCOUNTS (STOCK) ##################################

def export_bs():

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseprod']
                            )
    cursor = cnx.cursor()

    query = """
            SELECT date_format(date_cash, '%m-%y') as data, Conta, ROUND(sum(valor), 2) as Value, parent, code

                FROM (

                    SELECT parent, code, act_debit.report AS report, date_cash, debit AS Conta, SUM(CASE WHEN act_debit.nature = 0 THEN value ELSE -value END) AS valor 
                    FROM journal 
                    RIGHT JOIN accounts AS act_debit ON act_debit.account = journal.debit
                    GROUP BY debit, YEAR(date_cash), MONTH(date_cash)

                UNION

                    SELECT parent, code, act_credit.report AS report, date_cash, credit AS Conta, SUM(CASE WHEN act_credit.nature = 0 THEN value ELSE -value END) AS valor
                    FROM journal
                    RIGHT JOIN accounts AS act_credit ON act_credit.account = journal.credit
                    GROUP BY credit, YEAR(date_cash), MONTH(date_cash)

                ) AS aliastabela

            WHERE (report="Balance Sheet")
            GROUP BY Conta, YEAR(date_cash), MONTH(date_cash)
            ORDER BY date_cash ASC
            """

    df = pd.read_sql(query, cnx)
    report_bs = pd.pivot_table(df, values='Value', index='Conta', columns='data')

    print df







################################## EXPORT INCOME STATEMENT ACCOUNTS (FLOW) ##################################

def export_is():

    cnx = mariadb.connect(  user=cfg.db['user'],
                        password=cfg.db['pwd'],
                        database=cfg.db['baseprod']
                        )
    cursor = cnx.cursor()

    query = """
            SELECT date_format(date_cash, '%m-%y') as data, Conta, ROUND(sum(valor), 2) as Value, parent, code

                FROM (

                    SELECT parent, code, act_debit.report AS report, date_cash, debit AS Conta, SUM(CASE WHEN act_debit.nature = 0 THEN value ELSE -value END) AS valor 
                    FROM journal 
                    RIGHT JOIN accounts AS act_debit ON act_debit.account = journal.debit
                    GROUP BY debit, YEAR(date_cash), MONTH(date_cash)

                UNION

                    SELECT parent, code, act_credit.report AS report, date_cash, credit AS Conta, SUM(CASE WHEN act_credit.nature = 0 THEN value ELSE -value END) AS valor
                    FROM journal
                    RIGHT JOIN accounts AS act_credit ON act_credit.account = journal.credit
                    GROUP BY credit, YEAR(date_cash), MONTH(date_cash)

                ) AS aliastabela

            WHERE (report="Income Statement")
            GROUP BY Conta, YEAR(date_cash), MONTH(date_cash)
            ORDER BY date_cash ASC
            """

    df = pd.read_sql(query, cnx)
    report_is = pd.pivot_table(df, values='Value', index='Conta', columns='data')

    print df





################################## EXPORT HIGHCHART DATASET (FLOW) ##################################

def chart_test(chartID = 'chart_ID', chart_height = 350):

    print "test1"
    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseprod']
                            )
    cursor = cnx.cursor()

    # query_accounts =    """
    #                     SELECT account FROM accounts WHERE level = "Level 4"
    #                     """

    # cursor.execute(query_accounts)
    # accounts = cursor.fetchone()  

    conta = request.form['series']
    params = (conta, conta)

    query =  """
                SELECT 
                (
                    SUM(IF(credit="%s", value, 0))-
                    SUM(IF(debit="%s", value, 0))
                )
                AS fluxo    
                FROM journal
                GROUP BY YEAR(date_cash), MONTH(date_cash)
                ORDER BY date_cash ASC
                """ % (params)

    df = pd.read_sql(query, cnx)
    series = df['fluxo'].tolist()

    # window = request.select['window']

    mavg = df.rolling(window=6, center=False).mean()
    mavg = mavg.fillna("null")
    mavg = mavg['fluxo'].tolist()
    series_label = str(conta)
    cnx.commit()

    # query_datas =   """
    #                 SELECT DATE_FORMAT(date_cash, '%b-%y') FROM journal
    #                 GROUP BY month(date_cash), year(date_cash) ORDER BY date_cash ASC
    #                 """

    # datas = pd.read_sql(query_datas, cnx)
    # datas = df['date_cash'].tolist()
    # datas = [i[0] for i in rows]
    # cnx.commit()

    datas = [   "Abr-2015", "Mai-2015", "Jun-2015", "Jul-2015", "Ago-2015", "Set-2015", "Out-2015", "Nov-2015", "Dez-2015",
                "Jan-2016", "Fev-2016", "Mar-2016", "Abr-2016", "Mai-2016", "Jun-2016", "Jul-2016", "Ago-2016", "Set-2016",
                "Out-2016", "Nov-2016", "Dez-2016", "Jan-2017", "Fev-2017", "Mar-2017", "Abr-2017", "Mai-2017", "Jun-2017",
                "Jul-2017", "Ago-2017", "Set-2017", "Out-2017", "Nov-2017"]


    chart = {"renderTo": chartID, "height": chart_height}
    series1 = {"name": series_label, "data": series, "type": 'column'}
    series2 = {"name": 'Moving Average', "data": mavg, "type": 'spline'}
    title = {"text": 'Series Selecionadas'}
    xAxis = {"categories": datas, "crosshair": 'true'}
    yAxis = {"title": {"text": 'Valor'}}
    
    return render_template(
                            'reports.html',
                            chartID=chartID,
                            chart=chart,
                            series1=series1,
                            series2=series2,
                            title=title,
                            xAxis=xAxis,
                            yAxis=yAxis
                            )
