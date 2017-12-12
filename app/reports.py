from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import views




##################### EXPORT BALANCE SHEET ACCOUNTS (STOCK) #####################

def export_bs_data():

	pdc = "account_teste"
	level = "Level 4"
	report = "Balance Sheet"
	params = (pdc, level, report)

	cnx = mariadb.connect(  user=cfg.db['user'],
							password=cfg.db['pwd'],
							database=cfg.db['baseteste']
							)

	cursor = cnx.cursor()

	infos = """
			SELECT account FROM %s WHERE level = %s AND report = %s
			""" % (params)
	
	
	cursor.execute(infos)
	infos = cursor.fetchall()
	bs_accounts = list(infos)
	cnx.close()        

	for account in bs_accounts:
		cnx = mariadb.connect(  user=cfg.db['user'],
								password=cfg.db['pwd'],
								database=cfg.db['baseteste']
								)

		cursor = cnx.cursor()
		params = (account, account)
		
		query = """
				SELECT Y, M,(@total := @total + Fluxo) AS ValorTotal
				FROM (
				SELECT year(data) AS Y, month(data) AS M, 
					(
						SUM(IF(credit="%s", valor, 0))-
						SUM(IF(debit="%s", valor, 0))
					) AS Fluxo
					FROM journal_test
					GROUP BY YEAR(DATA), MONTH(DATA)
					) AS T,
				(SELECT @total:=0) AS n;
				""" % (params)

		cursor.execute(query)
		rows = cursor.fetchall()
		desc = cursor.description
		
		lista = [dict(itertools.izip([col[0] for col in desc], row)) 
			for row in rows]

		cnx.commit()
		cnx.close()

		print json.dumps(lista)

	return lista







##################### EXPORT INCOME STATEMENT ACCOUNTS (FLOW) #####################

def export_is_data():

	pdc = "account_teste"
	level = "Level 4"
	report = "Income Statement"
	params = (pdc, level, report)

	cnx = mariadb.connect(  user=cfg.db['user'],
							password=cfg.db['pwd'],
							database=cfg.db['baseteste']
							)

	cursor = cnx.cursor()

	infos = """
			SELECT account FROM %s WHERE level = %s AND report = %s
			""" % (params)
	
	
	cursor.execute(infos)
	infos = cursor.fetchall()
	is_accounts = list(infos)
	cnx.close()        

	for account in is_accounts:
		
		cnx = mariadb.connect(  user=cfg.db['user'],
								password=cfg.db['pwd'],
								database=cfg.db['baseteste']
								)

		cursor = cnx.cursor()
		params = (account, account)
		
		query = """
				SELECT year(data), month(data), 
					(
						SUM(IF(credit=%s, valor, 0))-
						SUM(IF(debit=%s, valor, 0))
					)
				AS Fluxo    
				FROM journal_test
				GROUP BY YEAR(data), MONTH(data)
				""" % (params)

		cursor.execute(query)
		rows = cursor.fetchall()
		desc = cursor.description
		
		lista = [dict(itertools.izip([col[0] for col in desc], row)) 
			for row in rows]

		cnx.commit()
		cnx.close()

		print json.dumps(lista)

	return lista









##################### EXPORT HIGHCHART DATASET (FLOW) #####################

def is_char_test(chartID = 'chart_ID', chart_type = 'areaspline', chart_height = 350):

	cnx = mariadb.connect(user='root', password='', database='base_teste')
	cursor = cnx.cursor()
	conta1 = "Beneficios"
	params1 = (conta1, conta1)

	query_is = """
			SELECT 
			(
				SUM(IF(Credito="%s", valor, 0))-
				SUM(IF(Debito="%s", valor, 0))
			)
			AS Fluxo	
			FROM journal_test
			GROUP BY YEAR(data), MONTH(data)
			ORDER BY Year(data), MONTH(data) DESC
			""" % params1


	cursor.execute(query_is)
	rows = cursor.fetchall()
	desc = cursor.description
	salario = [i[0] for i in rows]


	conta3 = "Estacionamento"
	params3 = (conta3, conta3)

	query_is2 = """
			SELECT 
			(
				SUM(IF(Credito="%s", valor, 0))-
				SUM(IF(Debito="%s", valor, 0))
			)
			AS Fluxo	
			FROM journal_test
			GROUP BY YEAR(data), MONTH(data)
			ORDER BY Year(data), MONTH(data) DESC
			""" % params3


	cursor.execute(query_is2)
	rows = cursor.fetchall()
	desc = cursor.description
	
	combustivel = [i[0] for i in rows]
	# lista = [dict(itertools.izip([col[0] for col in desc], row)) 
	# 	for row in rows]

	cnx.commit()

	query_datas = 	"""
					SELECT DATE_FORMAT(data, '%b-%y') FROM journal_test
					group by month(data), year(data) order by data asc
					"""

	cursor.execute(query_datas)
	rows = cursor.fetchall()
	desc = cursor.description
	# datas = [i[0] for i in rows]

	cnx.commit()

	datas = [ 	"Abr-2015", "Mai-2015", "Jun-2015", "Jul-2015", "Ago-2015", "Set-2015", "Out-2015", "Nov-2015", "Dez-2015",
				"Jan-2015", "Fev-2015", "Mar-2015", "Abr-2015", "Mai-2015", "Jun-2015", "Jul-2015", "Ago-2015", "Set-2015",
				"Out-2015", "Nov-2015", "Dez-2015", "Jan-2015", "Fev-2015", "Mar-2015", "Abr-2015", "Mai-2015", "Jun-2015",
				"Jul-2015", "Ago-2015", "Set-2015",	"Out-2015", "Nov-2015",]


	# print datas

	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Salario', "data": salario}, {"name": 'Combustivel', "data": combustivel}]
	title = {"text": 'Salario'}
	xAxis = {"categories": datas}
	yAxis = {"title": {"text": 'Valor'}}
	
	return render_template('reports.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
