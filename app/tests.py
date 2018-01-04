# -*- coding: latin-1 -*-

## We can use this to work on the project
# THis is what I have to far, you can run this code to see how the DataFrame is organized

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt




def GetISLevel():

    cnx = mariadb.connect(  user='root',
                            password='',
                            database='db_finp'
                            )

    cursor = cnx.cursor()

    level1 =    """
                SELECT code, account, parent
                FROM accounts
                WHERE level = 1
                AND report = "Income Statement"
                """

    cursor.execute(level1)
    rows = cursor.fetchall()
    desc = cursor.description
    is_l1_accounts = [dict(itertools.izip([col[0] for col in desc], row)) for row in rows]

    level2 =    """
                SELECT code, account, parent
                FROM accounts
                WHERE level = 2
                AND report = "Income Statement"
                """

    cursor.execute(level2)
    rows = cursor.fetchall()
    desc = cursor.description
    is_l2_accounts = [dict(itertools.izip([col[0] for col in desc], row)) for row in rows]

    level3 =    """
                SELECT code, account, parent
                FROM accounts
                WHERE level = 3
                AND report = "Income Statement"
                """

    cursor.execute(level3)
    rows = cursor.fetchall()
    desc = cursor.description
    is_l3_accounts = [dict(itertools.izip([col[0] for col in desc], row)) for row in rows]

    level4 =    """
                SELECT code, account, parent
                FROM accounts
                WHERE level = 4
                AND report = "Income Statement"
                """

    cursor.execute(level4)
    rows = cursor.fetchall()
    desc = cursor.description
    is_l4_accounts = [dict(itertools.izip([col[0] for col in desc], row)) for row in rows]

    chart = is_l4_accounts + is_l3_accounts + is_l2_accounts + is_l1_accounts
    chart = json.dumps(chart)

    return render_template('project1.html', isdata=dataset)
