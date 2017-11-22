import mysql.connector as mariadb
import json
import collections
import pymysql
import itertools
import io

print "1. iniciando programa..."

#Conecta base de dados e cria o cursor
cnx = mariadb.connect(user='root', password='', database='test')
cursor = cnx.cursor()
print "2. base conectada..."

#executa query
cursor.execute("SELECT ID, data, cred, deb, dsc, valor FROM base")
print "3. query realizada..."

#Pega base do MySQL
rows = cursor.fetchall()
print "4. dados captados..."

#Retorna todas as linhas de um cursor como uma lista de dicts.
def dictfetchall(cursor):
    desc = cursor.description
    return [dict(itertools.izip([col[0] for col in desc], row)) 
        for row in rows]

#Coloca o fetchall dentro de results
results = dictfetchall(cursor)

#Salva resultado no arquivo data.json
with open('static/files/data222.json', 'wb+') as fp:
    json.dump(results, fp)
