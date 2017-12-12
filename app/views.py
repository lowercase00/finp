from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import journal
import accounts
from reports import is_char_test



################# TEMPLATE VIEWS #################

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/_journal', methods=['GET', 'POST'])
def journal():
    return render_template("journal.html")


@app.route('/_reports')
def reports():
    return is_char_test()


@app.route('/_forecast')
def forecast():
    return render_template("forecast.html")


@app.route('/_budget')
def budget():
    return render_template("budget.html")


@app.route('/_accounts')
def accounts():
    return render_template("accounts.html")


@app.route('/_bills')
def bills():
    return render_template("bills.html")





################# TEMPLATE VIEWS #################

@app.route('/_jquerytabledit', methods=['GET', 'POST'])
def jquerytabledit():
    return render_template("jquerytabledit.html")


@app.route('/_datatable', methods=['GET', 'POST'])
def datatable():
    return render_template("datatable.html")


@app.route('/_editablegrid', methods=['GET', 'POST'])
def editablegrid():
    return render_template("editablegrid.html")


@app.route('/_xeditable', methods=['GET', 'POST'])
def xeditable():
    return render_template("xeditable.html")


@app.route('/_chartest', methods=['GET', 'POST'])
def chartest():
    return get_is_accounts()
