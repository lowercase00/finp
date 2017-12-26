## We can use this to work on the project
# THis is what I have to far, you can run this code to see how the DataFrame is organized


import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import pandas as pd


def makereport():

    cnx = mariadb.connect(  user='root',
                            password='',
                            database='db_finp'
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

    df          = pd.read_sql(query, cnx)
    df['data']  = pd.to_datetime(df['data'], format='%m-%y')
    df          = df.set_index(['data', 'parent', 'code'])
    report_is   = pd.pivot_table(df, values='Value', index=['parent', 'code', 'Conta'], columns='data')
    group       = df.groupby(['data', 'parent', 'Conta']).sum()
    json        = report_is.to_json()

    dataset     = df

    print report_is

    return render_template('project1.html', isdata=dataset)
