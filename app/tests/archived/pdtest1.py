import pandas
import mysql.connector as mariadb
import matplotlib.pyplot as plt
import json

# Takes the whole MySQL table and makes it a DataFrame in Pandas

cnx = mariadb.connect(user='root', password='', database='base_teste')
cursor = cnx.cursor()

query = """
		SELECT * FROM journal_test
		"""

journal = pandas.read_sql(query, cnx)


query = """
		SELECT account, code, parent FROM accounts_test
		"""

chart = pandas.read_sql(query, cnx)


#Transforms "Date Cash" strings into a DateTime object
journal['datecash'] = pandas.to_datetime(journal['datecash'])

#Group by year, month, summing the accounts
single_account = journal.groupby([pandas.Grouper(freq='MS',key='datecash')]).sum().unstack()

print single_account




# df_subset = df[(df.datecash == 1) & (df.D > 5)]
# df_subset.apply(lambda x: x.C * x.E, axis=1).sum()