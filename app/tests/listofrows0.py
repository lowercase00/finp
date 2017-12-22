import pandas
import mysql.connector as mariadb
import matplotlib.pyplot as plt
import json
import jsonify


####################### Income Statement - From MySQL Database to Pandas Dataframe
cnx = mariadb.connect(user='root', password='', database='db_finp')
cursor = cnx.cursor()

query = """
		SELECT DATE_FORMAT(date_cash, '%b-%y'), credit, debit, value FROM journal LIMIT 5
		"""

cursor.execute(query)
rows = cursor.fetchall()
desc = cursor.description
cnx.close()

list_of_rows = [list(i) for i in rows]

print list_of_rows