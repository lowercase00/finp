from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mariadb
import json, jsonify, collections, itertools, csv
import config as cfg
import views
import datetime




################################## EXPORT JOURNAL ##################################


## This gets all of the journal entries and sends it to Javascript to be rendered by
## the Datatable plug-in

def export_journal():
    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseprod']
                            )
    cursor = cnx.cursor()

    query = """
            SELECT CAST(ROUND(id,2) AS CHAR(10)),
            DATE_FORMAT(date_cash, '%b-%y'), credit, debit, CAST(ROUND(value,2) AS CHAR(10))
            FROM journal
            ORDER BY ID ASC
            """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    desc = cursor.description
    cnx.close()
    
    journal = [list(i) for i in rows]
    journal = [[s.encode('ascii', 'ignore') for s in i] for i in journal]


    return render_template('journal.html', journal=journal)




################################## MANUAL INPUT IN LEDGER ##################################


## Function to get the User input form the form and input it into the Journal on the database
##
def journal_entry():
    
    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseprod']
                            )
    cursor = cnx.cursor()
    
    add_reg =   """
                INSERT INTO journal
                (date_cash, credit, debit, description, value)
                VALUES (%s, %s, %s, %s, %s)
                """
	
    data    = request.form['data']
    cred    = request.form['credito']
    deb     = request.form['debito']
    desc    = request.form['descricao']
    valor   = request.form['valor']


    registro = (data, cred, deb, desc, valor)

    cursor.execute(add_reg, registro)
    cnx.commit()
    cnx.close()

    return redirect(url_for('journal'))





################################## CSV IMPORT IN LEDGER ##################################


## This will be a function to import an CSV upload to the journal, don't think it's working at the moment
##
def journal_import_csv():
    
    cnx = mariadb.connect(  user=cfg.db['user'],
                            password=cfg.db['pwd'],
                            database=cfg.db['baseprod']
                            )
    cursor = cnx.cursor()
    csv_data = csv.reader(file('journal.csv'))
    
    for row in csv_data:

        query = """
                INSERT INTO testcsv(date_cash, credit, debit, description, values),
                VALUES (%s, %s, %s, %s, %s)
                """ % (row)

        cursor.execute(query)
        cnx.commit()

    cnx.close()
    return redirect(url_for('journal'))





################################## ACCOUNT IMPORT IN LEDGER ##################################


## Future function to import only on account to the journal
##

# def journal_import_csv_account():

#     cnx = mariadb.connect(  user=cfg.db['user'],
#                         password=cfg.db['pwd'],
#                         database=cfg.db['baseprod']
#                         )
    
#     cursor = cnx.cursor()

#     account = form.request(input_account)
#     csv_data = imported_file()

#  # Credit accounts
#     if account_nature == 1:
    
#         for row in csv_data:

#             if value < 0:
                
#                 query = """
#                       INSERT INTO journal
#                       (date_cash, date_acc, credit, debit, description, value)
#                       VALUES (%s, %s, %s, %s, %s, %s)
#                       """ % (row, row, account, row, row, row)
            
#                 cursor.execute(query)
            

#              else
                
#                 query = """
#                       INSERT INTO journal_test
#                       (datecash, dateacc, credit, debit, description, value)
#                       VALUES (%s, %s, %s, %s, %s, %s)
#                       """ % (row, row, row, account, row, row)
            
#                 cursor.execute(query)

# # Debit accounts
#     else:
    
#         for row in csv_data:
        
#             if value > 0:
                
#                 query = """
#                       INSERT INTO journal_test
#                       (datecash, dateacc, credit, debit, description, value)
#                       VALUES (%s, %s, %s, %s, %s, %s)
#                       """ % (row, row, row, account, row, row)
                
#                 cursor.execute(query)
                

#             else:
                
#                 query = """
#                       INSERT INTO journal_test
#                       (datecash, dateacc, credit, debit, description, value)
#                       VALUES (%s, %s, %s, %s, %s, %s)
#                       """ % (row, row, account, row, row, row)
                
#                 cursor.execute(query)





# ##################### EDIT ENTRIES #####################

# def edit_ledger():    

    # Create cursor
    # cnx = mariadb.connect(  user='root',
    #                         password='',
    #                         database='test'
    #                         )

    # cursor = cnx.cursor()
    # result = cursor.execute("SELECT * FROM articles WHERE id = %s", [id])

    # article = cursor.fetchone()
    # cnx.close()
    # form = ArticleForm(request.form)

    # form.title.data = article['title']
    # form.body.data = article['body']

    # if request.method == 'POST' and form.validate():
    # title = request.form['title']
    # body = request.form['body']

    # app.logger.info(title)
    # cursor.execute ("UPDATE articles SET title=%s, body=%s WHERE id=%s",(title, body, id))
    # cnx.commit()
    # cnx.close()

    # flash('Article Updated', 'success')

    # return redirect(url_for('dashboard'))
    # return render_template('edit_article.html', form=form)








# ###################### DELETE ENTRIES #####################

# def delete_ledger():

    # # Create cursor
    # cnx = mariadb.connect(  user='root',
    #     password='',
    #     database='test'
    #     )
    # cursor = cnx.cursor()

    # # Execute
    # cursor.execute("DELETE FROM journal WHERE id = %s", [id])

    # # Commit to DB
    # cnx.commit()

    # #Close connection
    # cnx.close()

    # flash('Article Deleted', 'success')

    # return redirect(url_for('dashboard'))

