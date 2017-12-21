import pandas
import mysql.connector as mariadb
import matplotlib.pyplot as plt
import json
import jsonify


####################### Income Statement - From MySQL Database to Pandas Dataframe
cnx = mariadb.connect(user='root', password='', database='db_finp')
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
df['data'] = pandas.to_datetime(df['data'], format='%m-%y')
df = df.sort_values(by=['code'])

report_is = pandas.pivot_table(df, values='Value', index='Conta', columns='data')
report_is = report_is.fillna(0)
json_file = report_is.reset_index().to_json('file.json', orient='records')

print json_file