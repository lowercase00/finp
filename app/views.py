from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import journal
import accounts
from project import make_is_report
from reports import chart_test
from journal import export_journal



################# TEMPLATE VIEWS #################

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print request
    else: 
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
        return single_account()


@app.route('/_forecast')
def forecast():
    return render_template("forecast.html")



@app.route('/_tests')
def tests():
    return test_function()


@app.route('/_project')
def project():
    return make_is_report()






@app.route('/_chartest', methods=['GET', 'POST'])
def chartest():
    return get_is_accounts()
