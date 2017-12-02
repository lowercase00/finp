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


@app.route('/files', methods=['GET', 'POST'])
def files(**kwargs):
    return files


@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
	results = export_data()
	return results





@app.route('/jquerytableedit', methods=['GET', 'POST'])
def jquerytableedit():
    return render_template("jquerytableedit.html")


@app.route('/datatable', methods=['GET', 'POST'])
def datatable():
    return render_template("datatable.html")


@app.route('/editablegrid', methods=['GET', 'POST'])
def editablegrid():
    return render_template("editablegrid.html")


@app.route('/xeditable', methods=['GET', 'POST'])
def xeditable():
    return render_template("xeditable.html")