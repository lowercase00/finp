
#Soma conta para um determinado mês

SELECT 	(
			(SELECT SUM(valor) FROM base WHERE credito='Conta Corrente Itau' and MONTH(data)=10 and YEAR(data)=2017)
			-
			(SELECT SUM(valor) FROM base WHERE debito='Conta Corrente Itau' and MONTH(data)=10 and YEAR(data)=2017)
		)



#TimeSeries - conta quantas entradas por ano
SELECT YEAR(data) AS Year,COUNT(*) AS base FROM base GROUP BY YEAR(data);



#soma todas as movimentacoes agrupando por mes e ano
SELECT YEAR(data) AS Year,
MONTH(data) AS Month,
SUM(valor) AS base
FROM base_completa.base
GROUP BY YEAR(data),MONTH(data)



#soma todas as movimentacoes de uma conta especifica agrupando por mes e ano
SELECT data, base, (@total := @total + base) AS ValorTotal
FROM (
	SELECT data,
	SUM(VALOR)
	AS base 
	FROM base
	WHERE
		(debito="Conta Corrente Itau")
	GROUP BY YEAR(DATA), MONTH(DATA)
	) AS T,
(SELECT @total:=0) AS n;



# FLUXO - soma todas as movimentacoes de uma conta (credito + debito) e agrupa por mes/ano - apenas fluxo
SELECT year(data), month(data), 
	(
		SUM(IF(Credito='Conta Corrente Itau', valor, 0))-
		SUM(IF(Debito='Conta Corrente Itau', valor, 0))
	)
AS Fluxo	
FROM base
GROUP BY YEAR(data), MONTH(data)



# BALANCO - soma todas as movimentacoes de uma conta (credito + debito) e agrupa por mes/ano
SELECT Y, M,(@total := @total + Fluxo) AS ValorTotal
FROM (
        SELECT year(data) AS Y, month(data) AS M, 
            (
                SUM(IF(Credito='Conta Corrente Itau', valor, 0))-
                SUM(IF(Debito='Conta Corrente Itau', valor, 0))
            ) AS Fluxo
        FROM base
        GROUP BY YEAR(DATA), MONTH(DATA)
    ) AS T,
(SELECT @total:=0) AS n;

