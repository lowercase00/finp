import pandas as pd
import mysql.connector as mariadb
import matplotlib.pyplot as plt

# Pega resultado da query da MySQL e passa para DataFrame no Pandas

cnx = mariadb.connect(user='root', password='', database='base_completa')
cursor = cnx.cursor()

query = """SELECT year(data), month(data), 
			(
				SUM(IF(Credito='Conta Corrente Itau', valor, 0))-
				SUM(IF(Debito='Conta Corrente Itau', valor, 0))
			)
		AS Fluxo	
		FROM base
		GROUP BY YEAR(data), MONTH(data)"""

df = pd.read_sql(query, cnx)

cnx.close()

# print df
print df.to_json()
# df.plot()
# plt.show()
