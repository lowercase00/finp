from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv


def export_journal():
    cnx = mariadb.connect(  user='root',
                            password='',
                            database='db_finp'
                            )
    cursor = cnx.cursor()

    query = """
            SELECT ID, date_cash, credit, debit, description, value
            FROM journal
            ORDER BY date_cash DESC
            """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    desc = cursor.description
    cnx.close()
    
    journal = [list(i) for i in rows]

    # journal = [ ['item 1', 'item 2', 'item 3'],
    #             ['item 1', 'item 2', 'item 3'],
    #             ['item 1', 'item 2', 'item 3'],
    #             ['item 1', 'item 2', 'item 3'],
    #             ['item 1', 'item 2', 'item 3']]

    return journal

print export_journal()