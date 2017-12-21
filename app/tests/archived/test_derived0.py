from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv

def create_bs():

	pdc = "accounts"
	level = "Level 4"
	report = "Balance Sheet"
	params = (pdc, level, report)

	cnx = mariadb.connect(  user='root',
							password='',
							database='db_finp'
							)

	cursor = cnx.cursor()

	infos = """
			SELECT account FROM %s WHERE level = '%s' AND report = '%s'
			""" % (params)
	
	
	cursor.execute(infos)
	bs_accounts_results = cursor.fetchall()
	bs_accounts = [i[0] for i in bs_accounts_results]
	cnx.close() 

	for account in bs_accounts:
		cnx = mariadb.connect(  user='root',
								password='',
								database='db_finp'
								)

		cursor = cnx.cursor()
		params = (account, account)

		query = """
				SELECT (@total := @total + Fluxo) AS ValorTotal
				FROM (
					SELECT date_cash AS date, 
					(
						SUM(IF(credit="%s", value, 0))-
						SUM(IF(debit="%s", value, 0))
					) AS Fluxo
					FROM journal
					GROUP BY YEAR(date_cash), MONTH(date_cash)
					) AS T,
				(SELECT @total:=0) AS n;
				""" % (params)

		cursor.execute(query)
		rows = cursor.fetchall()
		desc = cursor.description
		bs_values = [i[0] for i in rows]


		cnx.commit()
		cnx.close()

		print bs_values
		break

	return bs_values

create_bs()
