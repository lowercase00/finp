#!/usr/bin/python
# coding=latin1

import mysql.connector as mariadb

#Conecta base de dados e cria o cursor
mariadb_connection = mariadb.connect(user='root', password='', database='test')
cursor = mariadb_connection.cursor()

#querys
query_saidas = ("SELECT SUM(valor) FROM base WHERE cred='Itau' and MONTH(data)=11 and YEAR(data)=2017")
query_entradas = ("SELECT SUM(valor) FROM base WHERE deb='Itau' and MONTH(data)=11 and YEAR(data)=2017")


#executa query de saidas
cursor.execute(query_saidas)
for query_saidas in cursor:
	query_saidas = int(query_saidas[0])


#executa query de entradas
cursor.execute(query_entradas)
for query_entradas in cursor:
	query_entradas = int(query_entradas[0])


#calcula saldo
saldo = query_entradas - query_saidas
saldo = int(saldo)

#output do saldo final
print "O saldo final é de",saldo

#fecha conexao
cursor.close()
mariadb_connection.close()