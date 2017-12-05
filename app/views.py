from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import ledger
import accounts
import reports




################# TEMPLATE VIEWS #################

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/_ledger', methods=['GET', 'POST'])
def ledger():
    return render_template("ledger.html")


@app.route('/_reports')
def reports():
    return render_template("reports.html")


@app.route('/_forecast')
def forecast():
    return render_template("forecast.html")


@app.route('/_pdc')
def pdc():
    return render_template("pdc.html")







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
