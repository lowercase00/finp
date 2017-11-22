import mysql.connector as mariadb
import json
import collections
import pymysql
import itertools
import io
# from app import app

print "1. iniciando programa..."
cnx = mariadb.connect(user='root', password='', database='test')
cursor = cnx.cursor()
print "2. base conectada..."

#executa query
cursor.execute("SELECT ID, data, cred, deb, dsc, valor FROM base")
print "3. query realizada..."

#Pega base do MySQL
rows = cursor.fetchall()
print "4. dados captados..."

# @app.route('/base_completa', methods=['GET', 'POST'])
def base_completa():
		#Conecta base de dados e cria o cursor

	#Retorna todas as linhas de um cursor como uma lista de dicts.
	def dictfetchall(cursor):
	    desc = cursor.description
	    return [dict(itertools.izip([col[0] for col in desc], row)) 
	        for row in rows]
	
	print "5. lista definida..."

	#Coloca o fetchall dentro de results
	results = dictfetchall(cursor)
	print "6. results gerado..."

	return results

print base_completa()

	#Salva resultado no arquivo data.json
	# with open('files/data.json', 'wb+') as fp:
	#     json.dump(results, fp)