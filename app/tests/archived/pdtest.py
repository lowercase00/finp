import pandas as pd
import mysql.connector as mariadb
import matplotlib.pyplot as plt
import json

# Pega resultado da query da MySQL e passa para DataFrame no Pandas

cnx = mariadb.connect(user='root', password='', database='base_teste')
cursor = cnx.cursor()


query = """
		SELECT datecash,(@total := @total + Fluxo) AS ValorTotal
		FROM (
	        SELECT datecash, 
	            (
	                SUM(IF(credit='Conta Corrente Itau', value, 0))-
	                SUM(IF(debit='Conta Corrente Itau', value, 0))
	            ) AS Fluxo
		        FROM journal_test
		        GROUP BY YEAR(datecash), MONTH(datecash)
		    ) AS T,
		(SELECT @total:=0) AS n;
		"""

df = pd.read_sql(query, cnx)
df['datecash'] = pd.to_datetime(df['datecash'])



print "Query realizada"
cnx.close()
print "Conexao encerrada"

print df
print "JSON Exportado."

# print df
# df.plot()
# plt.show()
