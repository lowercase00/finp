SELECT Y, M,(@total := @total + Fluxo) AS ValorTotal
FROM (
    SELECT year(data) AS Y, month(data) AS M, 
        (
            SUM(IF(Credito='%s', valor, 0))-
            SUM(IF(Debito='%s', valor, 0))
        ) AS Fluxo
        FROM ledger
        GROUP BY YEAR(DATA), MONTH(DATA)
    ) AS T,
(SELECT @total:=0) AS n;