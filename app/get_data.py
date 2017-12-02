import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv, json, jsonify, collections, itertools


#Export values for Balance Sheet Accounts (Stock/Accumulated Values)
def export_bs_data():

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )

    cursor = cnx.cursor()

    pdc = "pdc_teste"
    level = "Level 4"
    report = "Balance Sheet"
    params = (pdc, level, report)

    infos = """
    		SELECT account FROM %s WHERE level = %s AND report = %s
    		""" % (params)
    
    
    cursor.execute(infos)
    infos = cursor.fetchall()

    bs_accounts = list(infos)
    
    cnx.close()        

	#Loops through Balance Sheet accounts and retrieves accumulated values
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




#Export values for Income Statement Accounts (Flow Values)
def export_is_data():

	#Conects to database using config.py information
    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
							)

    cursor = cnx.cursor()

	#Parameters to get income statement accounts in specific chart of accounts table
    pdc = "pdc_teste"
    level = "Level 4"
    report = "Income Statement"
    params = (pdc, level, report)

    infos = """
    		SELECT account FROM %s WHERE level = %s AND report = %s
    		""" % (params)
    
    
    cursor.execute(infos)
    infos = cursor.fetchall()

    #income statement accounts turned into a list
    is_accounts = list(infos)
    
    cnx.close()        

    #loop through income statement accounts and dumps data into JSON format
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