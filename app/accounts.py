from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import views



################################## COMPLETE CHART OF ACCOUNTS ##################################


## Get's the full tree of accounts
##
def get_all_accounts():

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseprod']
                            )

    accounts = "accounts"
    params = (accounts, accounts, accounts, accounts)
    
    cursor = cnx.cursor()

    query = """
    SELECT
    t1.account AS Level1,
    t2.account AS Level2,
    t3.account AS Level3,
    t4.account AS Level4

    FROM %s AS t1

    LEFT JOIN %s AS t2 ON t2.parent = t1.code
    LEFT JOIN %s AS t3 ON t3.parent = t2.code
    LEFT JOIN %s AS t4 ON t4.parent = t3.code

    WHERE
    t1.account = 'Ativo' OR
    t1.account = 'Passivo' OR        
    t1.account = 'Receita' OR
    t1.account = 'Despesas' OR
    t1.account = 'Nao Operacionais';
    """ % (params)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    all_accounts = json.dumps(rows)

    return all_accounts




################################## BALANCE SHEET ACCOUNTS ##################################

## Gets all Balance Sheet accounts
##
def get_bs_accounts():

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )

    cursor = cnx.cursor()

    accounts = "accounts"
    params = (accounts, accounts, accounts, accounts)

    query = """
    SELECT
    t1.account AS Level1,
    t2.account AS Level2,
    t3.account AS Level3,
    t4.account AS Level4

    FROM %s AS t1

    LEFT JOIN %s AS t2 ON t2.parent = t1.code
    LEFT JOIN %s AS t3 ON t3.parent = t2.code
    LEFT JOIN %s AS t4 ON t4.parent = t3.code

    WHERE
    t1.account = 'Ativo' OR
    t1.account = 'Passivo';
    """ % (params)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    bs_accounts = json.dumps(rows)

    return bs_accounts





################################## INCOME STATEMENT ACCOUNTS ##################################

## Gets all Income Statement accounts
##
def get_is_accounts():

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['db_finp']
                            )

    cursor = cnx.cursor()

    accounts = "accounts"
    params = (accounts, accounts, accounts, accounts)

    query = """
    SELECT
    t1.account AS Level1,
    t2.account AS Level2,
    t3.account AS Level3,
    t4.account AS Level4

    FROM %s AS t1

    LEFT JOIN %s AS t2 ON t2.parent = t1.code
    LEFT JOIN %s AS t3 ON t3.parent = t2.code
    LEFT JOIN %s AS t4 ON t4.parent = t3.code

    WHERE
    t1.account = 'Receita' OR
    t1.account = 'Despesas' OR
    t1.account = 'Nao Operacionais';
    """ % (params)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    is_accounts = json.dumps(rows)

    return is_accounts

