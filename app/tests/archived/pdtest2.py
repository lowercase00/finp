import pandas
import mysql.connector as mariadb
import matplotlib.pyplot as plt
import json
import jsonify


####################### Income Statement - From MySQL Database to Pandas Dataframe
cnx = mariadb.connect(user='root', password='', database='db_finp')
cursor = cnx.cursor()

query = """
        SELECT 
        (
            SUM(IF(credit="%s", value, 0))-
            SUM(IF(debit="%s", value, 0))
        )
        AS Fluxo    
        FROM journal
        GROUP BY YEAR(date_cash), MONTH(date_cash)
        ORDER BY date_cash ASC
		"""

df = pandas.read_sql(query, cnx)
df['data'] = pandas.to_datetime(df['data'], format='%m-%y')
df = df.sort_values(by=['code'])

report_is = pandas.pivot_table(df, values='Value', index='Conta', columns='data')
report_is = report_is.fillna(0)
json_file = report_is.reset_index().to_json('file.json', orient='records')

print json_file