from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import journal
import accounts
from tests import test_function
from reports import chart_test
from journal import export_journal



################# TEMPLATE VIEWS #################

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/_journal', methods=['GET', 'POST'])
def journal():
    return export_journal()


@app.route('/_accounts')
def accounts():
    return render_template("accounts.html")


@app.route('/_reports', methods=['GET', 'POST'])
def reports():        
    if request.method == "GET":
        return render_template("reports.html")
    else:
        return chart_test()


@app.route('/_forecast')
def forecast():
    return render_template("forecast.html")



@app.route('/_tests')
def tests():
    return test_function()








################# TEMPLATE VIEWS #################


@app.route('/_datatable', methods=['GET', 'POST'])
def datatable():
    return render_template("datatable.html")



@app.route('/_jquerytabledit', methods=['GET', 'POST'])
def jquerytabledit():
    return render_template("jquerytabledit.html")



@app.route('/_editablegrid', methods=['GET', 'POST'])
def editablegrid():
    return render_template("editablegrid.html")


@app.route('/_xeditable', methods=['GET', 'POST'])
def xeditable():
    return render_template("xeditable.html")


@app.route('/_chartest', methods=['GET', 'POST'])
def chartest():
    return get_is_accounts()
