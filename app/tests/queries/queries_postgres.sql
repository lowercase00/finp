
########################## Sum of all credit values of a certain category, grouped by month (FLOW)	
SELECT 	sum("db_finp"."journal"."value") AS "sum", date_trunc('month', CAST("db_finp"."journal"."date_cash" AS timestamp)) AS "date_cash"
FROM "db_finp"."journal"
WHERE "db_finp"."journal"."credit" = 'Conta Corrente Itau'
GROUP BY date_trunc('month', CAST("db_finp"."journal"."date_cash" AS timestamp))
ORDER BY date_trunc('month', CAST("db_finp"."journal"."date_cash" AS timestamp)) ASC


########################## Shows the average spending for them month of all debit values of a certain category, grouped by month (FLOW)	
SELECT avg("db_finp"."journal"."value") AS "avg", date_trunc('month', CAST("db_finp"."journal"."date_cash" AS timestamp)) AS "date_cash"
FROM "db_finp"."journal"
WHERE "db_finp"."journal"."debit" = 'Bares & Bebidas'
GROUP BY date_trunc('month', CAST("db_finp"."journal"."date_cash" AS timestamp))
ORDER BY date_trunc('month', CAST("db_finp"."journal"."date_cash" AS timestamp)) ASC


######################## Shows all accounts of a certain level
SELECT	"db_finp"."accounts"."account" as account
FROM db_finp.accounts
WHERE db_finp.accounts.level = 'Level 4'


######################## Shows all accounts of a certain level of a certain report
SELECT	"db_finp"."accounts"."account" as account
FROM db_finp.accounts
WHERE db_finp.accounts.level = 'Level 4' AND db_finp.accounts.report = 'Income Statement'


######################## Creates a function to retrieve list of low level accounts in a certain report
CREATE TYPE get_accounts_results AS ARRAY[];

CREATE OR REPLACE FUNCTION get_accounts(report TEXT) RETURNS get_accounts_results AS

    $$ 
        SELECT  "db_finp"."accounts"."account" as account
        FROM db_finp.accounts
        WHERE db_finp.accounts.level = 'Level 4' AND db_finp.accounts.report = $1
    $$

    LANGUAGE SQL;

SELECT get_accounts('Income Statement') AS report_account;
