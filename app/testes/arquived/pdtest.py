import pandas as pd
import mysql.connector as mariadb
import matplotlib.pyplot as plt
import json

# Pega resultado da query da MySQL e passa para DataFrame no Pandas

cnx = mariadb.connect(user='root', password='', database='base_completa')
cursor = cnx.cursor()


query = """
		SELECT Y, M,(@total := @total + Fluxo) AS ValorTotal
		FROM (
	        SELECT year(data) AS Y, month(data) AS M, 
	            (
	                SUM(IF(Credito='Conta Corrente Itau', valor, 0))-
	                SUM(IF(Debito='Conta Corrente Itau', valor, 0))
	            ) AS Fluxo
		        FROM ledger
		        GROUP BY YEAR(DATA), MONTH(DATA)
		    ) AS T,
		(SELECT @total:=0) AS n;
		"""

df = pd.read_sql(query, cnx)
df.to_json()
print "Query realizada"
cnx.close()
print "Conexao encerrada"

with open('databp.json', 'wb+'):
    df.to_json()

print "JSON Exportado."

# print df
# df.plot()
# plt.show()
