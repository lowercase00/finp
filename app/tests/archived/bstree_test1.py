import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv, json, jsonify, collections, itertools
from ... import config as cfg

def export_balance_sheet():

	cnx = mariadb.connect(user='root', password='', database='test')
	cursor = cnx.cursor()

	pdc = "pdc_teste"

	query = """
			SELECT
				t1.account AS Level1,
				t2.account AS Level2,
				t3.account AS Level3,
				t4.account AS Level4

			FROM %s AS t1

			LEFT JOIN pdc_teste AS t2 ON t2.parent = t1.code
			LEFT JOIN pdc_teste AS t3 ON t3.parent = t2.code
			LEFT JOIN pdc_teste AS t4 ON t4.parent = t3.code

			WHERE
				t1.account = 'Ativo' OR
				t1.account = 'Passivo';
			""" % (pdc)
	
	cursor.execute(query)
	rows = cursor.fetchall()
	desc = cursor.description
	cnx.close()        
		
	lista = [dict(itertools.izip([col[0] for col in desc], row)) 
		for row in rows]

	cnx.close()

	bs_tree = json.dumps(lista)

	with open('bs_tree.json', 'wb+') as fp:
		json.dump(bs_tree, fp)

results = export_balance_sheet()