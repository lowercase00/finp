from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import datetime

def export_ledger():

    cnx = mariadb.connect(user='root', password='', database='base_teste')
    cursor = cnx.cursor()

    query = """
            SELECT DATE_FORMAT(datecash, '%m-%y')
            FROM journal_test
            GROUP BY  year(datecash), month(datecash)
            ORDER BY id DESC
            """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    desc = cursor.description
    cnx.close()

    dates = [i[0] for i in rows]
    dates = dates.strptime(dates)

    return dates

print export_ledger()