import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv, json, jsonify, collections, itertools

# Export calculations for each account


def export_data():

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )

    cursor = cnx.cursor()

    level = "nivel4"

    infos = """
    		SELECT %s FROM pdc
    		""" % (level)
    
    cursor.execute(infos)
    infos = cursor.fetchall()

    chart_of_accounts = list(infos)
    
    cnx.close()        

	for account in chart_of_accounts:
		
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

results = export_data()