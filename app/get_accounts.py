import mysql.connector as mariadb
from flask import Flask, render_template, request, redirect, url_for
import csv, json, jsonify, collections, itertools
import config as cfg



############## BALANCE SHEET ACCOUNTS #############


def get_bs_accounts():

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )

    cursor = cnx.cursor()

    pdc = "pdc_teste"
    params = (pdc, pdc, pdc, pdc)

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





############## INCOME STATEMENT ACCOUNTS #############


def get_is_accounts():

    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseteste']
                            )

    cursor = cnx.cursor()

    pdc = "pdc_teste"
    params = (pdc, pdc, pdc, pdc)

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
    t1.account = 'Não Operacionais';
    """ % (params)

    cursor.execute(query)
    rows = cursor.fetchall()        
    cnx.commit()
    is_accounts = json.dumps(rows)

