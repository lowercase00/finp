# views.py

from flask import render_template
from app import app
from app import data_cnx


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


@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
	results = export_data()
	return json.dumps(results)