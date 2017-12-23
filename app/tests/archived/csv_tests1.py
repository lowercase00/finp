import csv


############# Print each row as a dictionariy
with open('pdc.csv') as file:
	read = csv.DictReader(file)

	counter = 0

	for row in read:
		print row

		if counter > 5:
			break

		counter += 1


############# Print specific row as a dictionariy - use a key
with open('pdc.csv') as file:
	read = csv.DictReader(file)

	counter = 0

	for row in read:
		print(row['Account'])

		if counter > 5:
			break

		counter += 1



# ############# Print each row as a List
# with open('pdc.csv') as file:
# 	read = csv.Reader(file)

# 	counter = 0

# 	for row in read:
# 		print row

# 		if counter > 5:
# 			break

# 		counter += 1



# ############# Print specific row as a List
# with open('pdc.csv') as file:
# 	read = csv.Reader(file)

# 	counter = 0

# 	for row in read:
# 		print row

# 		if counter > 5:
# 			break

# 		counter += 1