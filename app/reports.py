from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import views




##################### EXPORT BALANCE SHEET ACCOUNTS (STOCK) #####################

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

    df = pandas.read_sql(query, cnx)
    report_bs = pandas.pivot_table(df, values='Value', index='Conta', columns='data')

    print df







##################### EXPORT INCOME STATEMENT ACCOUNTS (FLOW) #####################

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

    df = pandas.read_sql(query, cnx)
    report_is = pandas.pivot_table(df, values='Value', index='Conta', columns='data')

    print df







##################### EXPORT HIGHCHART DATASET (FLOW) #####################

def chart_test(chartID = 'chart_ID', chart_type = 'areaspline', chart_height = 350):

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
    testaccounts = [1, 2, 3, 4, 5]


    conta1 = request.form['series1']
    # conta1 = "Estacionamento"
    params1 = (conta1, conta1)

    query_is =  """
                SELECT 
                (
                    SUM(IF(credit="%s", value, 0))-
                    SUM(IF(debit="%s", value, 0))
                )
                AS Fluxo    
                FROM journal
                GROUP BY YEAR(date_cash), MONTH(date_cash)
                ORDER BY date_cash ASC
                """ % params1


    cursor.execute(query_is)
    rows = cursor.fetchall()
    desc = cursor.description
    series1 = [i[0] for i in rows]

    conta2 = request.form['series2']
    # conta2 = "Salario"
    params2 = (conta2, conta2)

    query_is2 = """
                SELECT 
                (
                    SUM(IF(credit="%s", value, 0))-
                    SUM(IF(debit="%s", value, 0))
                )
                AS Fluxo    
                FROM journal
                GROUP BY YEAR(date_cash), MONTH(date_cash)
                ORDER BY date_cash ASC
                """ % params2


    cursor.execute(query_is2)
    rows = cursor.fetchall()
    desc = cursor.description
    
    series2 = [i[0] for i in rows]
    # lista = [dict(itertools.izip([col[0] for col in desc], row)) 
    #   for row in rows]

    cnx.commit()

    query_datas =   """
                    SELECT DATE_FORMAT(date_cash, '%b-%y') FROM journal
                    GROUP BY month(date_cash), year(date_cash) ORDER BY date_cash ASC
                    """

    cursor.execute(query_datas)
    rows = cursor.fetchall()
    desc = cursor.description
    # datas = [i[0] for i in rows]

    cnx.commit()

    datas = [   "Abr-2015", "Mai-2015", "Jun-2015", "Jul-2015", "Ago-2015", "Set-2015", "Out-2015", "Nov-2015", "Dez-2015",
                "Jan-2015", "Fev-2015", "Mar-2015", "Abr-2015", "Mai-2015", "Jun-2015", "Jul-2015", "Ago-2015", "Set-2015",
                "Out-2015", "Nov-2015", "Dez-2015", "Jan-2015", "Fev-2015", "Mar-2015", "Abr-2015", "Mai-2015", "Jun-2015",
                "Jul-2015", "Ago-2015", "Set-2015", "Out-2015", "Nov-2015"]


    # print datas

    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'label', "data": series1}, {"name": 'label', "data": series2}]
    title = {"text": 'Series Selecionadas'}
    xAxis = {"categories": datas}
    yAxis = {"title": {"text": 'Valor'}}
    
    return render_template('reports.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis, testaccounts=testaccounts)
