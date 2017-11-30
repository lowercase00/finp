import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv, json, jsonify, collections, itertools

def export_data():
    
    infos = [
            'nivel1',
            'nivel2',
            'nivel3',
            'nivel4'
            ]

    levels = list(infos)

    for level in levels:
        
        cnx = mariadb.connect(user='root', password='', database='base_completa')
        cursor = cnx.cursor()

        query = """
                SELECT %s FROM pdc
                """ % (level)

        cursor.execute(query)
        rows = cursor.fetchall()        
        cnx.commit()

        print level
        print json.dumps(rows)

results = export_data()