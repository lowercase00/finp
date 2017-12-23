import pandas as pd
import mysql.connector as mariadb
import matplotlib.pyplot as plt
import json
import jsonify


####################### Income Statement - From MySQL Database to Pandas Dataframe
cnx = mariadb.connect(user='root', password='', database='db_finp')
cursor = cnx.cursor()

conta = "salario"
params = (conta, conta)
query = """
        SELECT 
        (
            SUM(IF(credit="%s", value, 0))-
            SUM(IF(debit="%s", value, 0))
        )
        AS fluxo    
        FROM journal
        GROUP BY YEAR(date_cash), MONTH(date_cash)
        ORDER BY date_cash ASC
		""" % params

df = pd.read_sql(query, cnx)
df_series = df['fluxo'].tolist()
df_avg = df.rolling(window=6, center=False).mean()
df_avg = df_avg['fluxo'].tolist()


print df_avg
