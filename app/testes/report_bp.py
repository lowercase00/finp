
chart_of_accounts_query = "SELECT COUNT(*) FROM accounts"

balance_sheet = {}

for account in chart_of_accounts:


	get_conta_bp = 	"""
					SELECT Y, M,(@total := @total + Fluxo) AS ValorTotal
					FROM (
					        SELECT year(data) AS Y, month(data) AS M, 
					            (
					                SUM(IF(Credito='%s', valor, 0))-
					                SUM(IF(Debito='%s', valor, 0))
					            ) AS Fluxo
					        FROM base
					        GROUP BY YEAR(DATA), MONTH(DATA)
					    ) AS T,
					(SELECT @total:=0) AS n;
					"""
	
	contas = ()

	query = (get_conta_bp, contas)
	
	df = pd.read_sql(query, cnx)
