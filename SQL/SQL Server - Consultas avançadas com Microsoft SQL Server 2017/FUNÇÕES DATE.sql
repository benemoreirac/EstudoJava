SELECT SYSDATETIME() -- DATA DO SITEMA

SELECT SYSDATETIMEOFFSET() --O -3 QUANTOS FUSO EM REALA��O A GRENWICH

SELECT SYSUTCDATETIME() -- HORARIO DE GREN

SELECT CURRENT_TIMESTAMP -- N�O � PRECISO OS MIN E SEGUNDOS

SELECT GETDATE() -- DATA/HORA LOCAL

SELECT GETUTCDATE() -- DATA/HORARIO PADRAO

SELECT DATENAME(YEAR, GETDATE()) -- RETORNA O ANO DA DATA ATUAL

SELECT DATENAME(MICROSECOND, GETDATE())

SELECT DATENAME(MONTH, GETDATE()) -- RETORNA O ANO DA DATA

SELECT DATEPART(MONTH, GETDATE()) --RETORNA O NOME DO MES

SELECT DAY(GETDATE()) -- RETORNA O DIA ATUAL

SELECT DATEFROMPARTS(2015,9,1)
SELECT DATENAME(MONTH, DATEFROMPARTS(2015,9,1))

SELECT DATETIME2FROMPARTS(2015,9,1,13,12,11,120,4) -- CRIAR DATA COM PRECISAO HORA/MIN/SEG

SELECT DATEDIFF(MONTH, DATEFROMPARTS(2015,9,1), GETDATE())

SELECT DATEADD(MONTH, 5, GETDATE())

SELECT ISDATE('2018-01-01')

SELECT ISDATE ('2018-25-28')

SELECT [DATA], CONCAT (DATENAME(DAY,[DATA]), ' DE ', DATENAME(MONTH, [DATA]), ' DE ' , DATENAME(YEAR, [DATA])) FROM [NOTAS FISCAIS]

SELECT NOME, DATEDIFF(YEAR, C.[DATA DE NASCIMENTO], GETDATE()) IDADE FROM [TABELA DE CLIENTES] AS C