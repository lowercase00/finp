import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv, json, jsonify, collections, itertools


############## CONTAS POR NIVEL #############


def get_level1_accounts():
    
    level = "nivel1"

    cnx = mariadb.connect(user='root', password='', database='base_completa')
    cursor = cnx.cursor()

    query = """
            SELECT DISTINCT(%s) FROM pdc
            """ % (level)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    level1_accounts = json.dumps(rows)



def get_level2_accounts():
    
    level = "nivel2"

    cnx = mariadb.connect(user='root', password='', database='base_completa')
    cursor = cnx.cursor()

    query = """
            SELECT DISTINCT(%s) FROM pdc
            """ % (level)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    level2_accounts = json.dumps(rows)



def get_level3_accounts():
    
    level = "nivel3"

    cnx = mariadb.connect(user='root', password='', database='base_completa')
    cursor = cnx.cursor()

    query = """
            SELECT DISTINCT(%s) FROM pdc
            """ % (level)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    level3_accounts = json.dumps(rows)



def get_level4_accounts():
    
    level = "nivel4"

    cnx = mariadb.connect(user='root', password='', database='base_completa')
    cursor = cnx.cursor()

    query = """
            SELECT DISTINCT(%s) FROM pdc
            """ % (level)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    level4_accounts = json.dumps(rows)






############## CONTAS POR NIVEL POR RELATORIO #############


def get_level4_bs_accounts():
    
    level = "nivel4"
    report = "Balance Sheet"
    params = (level, report)

    cnx = mariadb.connect(user='root', password='', database='base_completa')
    cursor = cnx.cursor()

    query = """
            SELECT DISTINCT(%s) FROM pdc WHERE report="%s"
            """ % (params)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    level4_bs_accounts = json.dumps(rows)
    level4_bs_accounts_list = list(rows)




def get_level4_is_accounts():
    
    level = "nivel4"
    report = "Income Statement"
    params = (level, report)

    cnx = mariadb.connect(user='root', password='', database='base_completa')
    cursor = cnx.cursor()

    query = """
            SELECT DISTINCT(%s) FROM pdc WHERE report="%s"
            """ % (params)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    level4_is_accounts = json.dumps(rows)
    level4_is_accounts_list = list(rows)   