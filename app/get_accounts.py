import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv, json, jsonify, collections, itertools
import config as cfg

#Exports chart of account by level, and/or by report

############## CONTAS POR NIVEL #############


def get_level1_accounts():
    
    level = "nivel2"
    table = "pdc_teste"
    params = (level, table)

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )

    cursor = cnx.cursor()

    query = """
            SELECT DISTINCT(%s)
            FROM %s
            """ % (params)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    level1_accounts = json.dumps(rows)



def get_level2_accounts():
    
    level = "nivel2"
    table = "pdc_teste"
    params = (level, table)

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )

    cursor = cnx.cursor()

    query = """
            SELECT DISTINCT(%s)
            FROM %s
            """ % (params)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    level2_accounts = json.dumps(rows)



def get_level3_accounts():
    
    level = "nivel3"
    table = "pdc_teste"
    params = (level, table)

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )

    cursor = cnx.cursor()

    query = """
            SELECT DISTINCT(%s)
            FROM %s
            """ % (params)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    level3_accounts = json.dumps(rows)



def get_level4_accounts():
    
    level = "nivel4"
    table = "pdc_teste"
    params = (level, table)

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )
    
    cursor = cnx.cursor()

    query = """
            SELECT DISTINCT(%s)
            FROM %s
            """ % (params)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    level4_accounts = json.dumps(rows)






############## CONTAS POR NIVEL POR RELATORIO #############


def get_level4_bs_accounts():
    
    level = "nivel4"
    report = "Balance Sheet"
    table = "pdc_teste"

    params = (level, table, report)

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )
    
    cursor = cnx.cursor()

    query = """
            SELECT DISTINCT(%s)
            FROM %s
            WHERE report="%s"
            """ % (params)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    level4_bs_accounts = json.dumps(rows)
    level4_bs_accounts_list = list(rows)




def get_level4_is_accounts():
    
    level = "nivel4"
    report = "Income Statement"
    table = "pdc_teste"

    params = (level, table, report)

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )
    
    cursor = cnx.cursor()

    query = """
            SELECT DISTINCT(%s)
            FROM %s
            WHERE report="%s"
            """ % (params)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    level4_is_accounts = json.dumps(rows)
    level4_is_accounts_list = list(rows)   