from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import views




##################### EXPORT BALANCE SHEET ACCOUNTS (STOCK) #####################

def export_bs_data():

	pdc = "pdc_teste"
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
						SUM(IF(Credito="%s", valor, 0))-
						SUM(IF(Debito="%s", valor, 0))
					) AS Fluxo
					FROM ledger_teste
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

	pdc = "pdc_teste"
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
						SUM(IF(Credito=%s, valor, 0))-
						SUM(IF(Debito=%s, valor, 0))
					)
				AS Fluxo    
				FROM base
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