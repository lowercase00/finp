# import csv
# import MySQLdb

# mydb = MySQLdb.connect(host='localhost',
#     user='root',
#     passwd='',
#     db='mydb')
# cursor = mydb.cursor()

# csv_data = csv.reader(file('students.csv'))
# for row in csv_data:

#     cursor.execute('INSERT INTO testcsv(names, \
#           classes, mark )' \
#           'VALUES(%s, %s, %s)', 
#           row)
# #close the connection to the database.
# mydb.commit()
# cursor.close()
# print "Done"




# def import_csv():
# 	account = form.request(input_account)
# 	csv_data = imported_file()

# 	if account_nature == credit:
	
# 		for row in csv_data:
	
# 			for value < 0 in row:
# 				query = """
# 						INSERT INTO journal_test
# 						(datecash, dateacc, credit, debit, description, value)
# 						VALUES (%s, %s, %s, %s, %s, %s)
# 						""" % (row, row, account, row, row, row)
# 				cursor.execute(query)
			

# 			for value > 0 in row:
# 				query = """
# 						INSERT INTO journal_test
# 						(datecash, dateacc, credit, debit, description, value)
# 						VALUES (%s, %s, %s, %s, %s, %s)
# 						""" % (row, row, row, account, row, row)
# 				cursor.execute(query)

	
# 		else:
	
# 			for row in csv_data:
		
# 				for value < 0 in row:
# 					query = """
# 							INSERT INTO journal_test
# 							(datecash, dateacc, credit, debit, description, value)
# 							VALUES (%s, %s, %s, %s, %s, %s)
# 							""" % (row, row, row, account, row, row)
# 					cursor.execute(query)
				

# 				for value > 0 in row:
# 					query = """
# 							INSERT INTO journal_test
# 							(datecash, dateacc, credit, debit, description, value)
# 							VALUES (%s, %s, %s, %s, %s, %s)
# 							""" % (row, row, account, row, row)
# 					cursor.execute(query)