
import pandas as pd
import mysql.connector as mariadb
import matplotlib.pyplot as plt

# Pega resultado da query da MySQL e passa para DataFrame no Pandas

cnx = mariadb.connect(user='root', password='', database='base_completa')
cursor = cnx.cursor()

chart_of_accounts = [
					'Conta Corrente Itau',
					'Cartao Itau Master',
					'Cartao Itau VISA',
					'Carteira'
					]

placeholders = '?' # For SQLite. See DBAPI paramstyle.
placeholders = ', '.join(placeholders for account in chart_of_accounts)

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

results = cursor.execute(query, (placeholders))
print results




# df = pd.read_sql(query, chart_of_accounts)
# print df.to_json()


# placeholder = '?' # For SQLite. See DBAPI paramstyle.
# placeholders = ', '.join(placeholder for unused in l)
# query = 'SELECT name FROM students WHERE id IN (%s)' % placeholders




# chart_of_accounts_query = "SELECT * FROM accounts"

# balance_sheet = 




# for account in chart_of_accounts:


# 	get_conta_bp = 	"""
# 					SELECT Y, M,(@total := @total + Fluxo) AS ValorTotal
# 					FROM (
# 					        SELECT year(data) AS Y, month(data) AS M, 
# 					            (
# 					                SUM(IF(Credito='%s', valor, 0))-
# 					                SUM(IF(Debito='%s', valor, 0))
# 					            ) AS Fluxo
# 					        FROM base
# 					        GROUP BY YEAR(DATA), MONTH(DATA)
# 					    ) AS T,
# 					(SELECT @total:=0) AS n;
# 					"""
	
# 	contas = ()

# 	query = (get_conta_bp, contas)
	
# 	df = pd.read_sql(query, cnx)
