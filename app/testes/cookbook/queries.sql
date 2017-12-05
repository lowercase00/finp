
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



#Pegar plano de contas
SELECT nivel4 FROM pdc



#Adicionar ID baseado na ordem de alguma coluna
ALTER TABLE ledger_teste ADD COLUMN new_id INT NOT NULL;
SET @x = 0;
UPDATE ledger_teste SET new_id = (@x:=@x+1) ORDER BY data ASC;
ALTER TABLE ledger_teste ADD PRIMARY KEY new_id (new_id);
ALTER TABLE ledger_teste CHANGE new_id new_id INT NOT NULL AUTO_INCREMENT;



#Substituir texto
UPDATE [tablename]
SET [fieldname] = REPLACE([fieldname], 'text to find', 'text to replace with')
WHERE [fieldname] LIKE '%text to find%'

UPDATE ledger_teste
SET Debito = REPLACE(Debito, 'Poupanca', 'Poupança')
WHERE Debito LIKE '%Poupanca%'


#Mostrar arvore para Balance Sheet
SELECT
t1.account AS Level1,
t2.account AS Level2,
t3.account AS Level3,
t4.account AS Level4

FROM pdc_teste AS t1

LEFT JOIN pdc_teste AS t2 ON t2.parent = t1.code
LEFT JOIN pdc_teste AS t3 ON t3.parent = t2.code
LEFT JOIN pdc_teste AS t4 ON t4.parent = t3.code

WHERE
t1.account = 'Ativo' OR
t1.account = 'Passivo';

#Mostrar arvore para Income Statement
SELECT
t1.account AS Level1,
t2.account AS Level2,
t3.account AS Level3,
t4.account AS Level4

FROM pdc_teste AS t1

LEFT JOIN pdc_teste AS t2 ON t2.parent = t1.code
LEFT JOIN pdc_teste AS t3 ON t3.parent = t2.code
LEFT JOIN pdc_teste AS t4 ON t4.parent = t3.code

WHERE
t1.account = 'Receitas' OR
t1.account = 'Despesas' OR
t1.account = 'Não Operacionais';
