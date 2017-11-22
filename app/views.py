# views.py

from flask import render_template

from app import app
from app import process
from app import base_completa


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/ledger', methods=['GET', 'POST'])
def ledger():
    return render_template("ledger.html")

@app.route('/reports')
def reports():
    return render_template("reports.html")

@app.route('/forecast')
def forecast():
    return render_template("forecast.html")

@app.route('/pdc')
def pdc():
    return render_template("pdc.html")

@app.route('/testes', methods=['GET', 'POST'])
def testes():
    return render_template("testes.html")

@app.route('/files', methods=['GET', 'POST'])
def files(**kwargs):
    return files