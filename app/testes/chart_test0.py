import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv, json, jsonify, collections, itertools


def data_test():

	cnx = mariadb.connect(user='root', password='', database='base_teste')

	cursor = cnx.cursor()

	account = "Salario"
	table = "ledger_teste"
	params = (account, account, table)

	query = """
			SELECT year(data), month(data), 
				(
					SUM(IF(Credito="Salario", valor, 0))-
					SUM(IF(Debito="Salario", valor, 0))
				)
			AS Fluxo    
			FROM ledger_teste
			GROUP BY YEAR(data), MONTH(data)
			"""
	
	
	cursor.execute(query)
	query_time_series = cursor.fetchall()

	cnx.close()
	
	return query_time_series


def FetchOneAssoc():
	
	cnx = mariadb.connect(user='root', password='', database='base_teste')
	cursor = cnx.cursor()

	query = """
		SELECT year(data), month(data), 
			(
				SUM(IF(Credito="Salario", valor, 0))-
				SUM(IF(Debito="Salario", valor, 0))
			)
		AS Fluxo    
		FROM ledger_teste
		GROUP BY YEAR(data), MONTH(data)
		"""

	cursor.execute(query)

	data = cursor.fetchone()
	
	if data == None:
			return None
	
	desc = cursor.description

	dict = {}
	
	for (name, value) in zip(desc, data):
		dict[name[0]] = value

	cnx.close()

	return dict



def TestFetch():
	
	cnx = mariadb.connect(user='root', password='', database='base_teste')
	cursor = cnx.cursor()

	query = """
		SELECT year(data), month(data), 
			(
				SUM(IF(Credito="Salario", valor, 0))-
				SUM(IF(Debito="Salario", valor, 0))
			)
		AS Fluxo    
		FROM ledger_teste
		GROUP BY YEAR(data), MONTH(data)
		"""

	cursor.execute(query)
	rows = cursor.fetchall()
		
	desc = cursor.description
	
	lista = [dict(itertools.izip([col[0] for col in desc], row)) 
		for row in rows]

	cnx.close()

	return lista

print TestFetch()


