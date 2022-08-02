/* -----------------------TABELAS TEMPOR�RIAS -----------  */
-- #TABELAS QUE VALEM PARA CONEX�O VIGENTE
CREATE TABLE #TABELA01 (ID VARCHAR(10) NULL, NOME VARCHAR(200)NULL)
INSERT INTO #TABELA01 (ID,NOME) VALUES('1','Jo�o')
SELECT * FROM #TABELA01
INSERT INTO #TABELA01 (ID,NOME) VALUES('2','Pedro')

SELECT * FROM ##TABELA02

-------------------------------------------------------------------
-- ## TABELAS QUE VALEM PARA VARIAS CONEXOES

CREATE TABLE ##TABELA02 (ID VARCHAR(10) NULL, NOME VARCHAR(200)NULL)
INSERT INTO ##TABELA02 (ID,NOME) VALUES('1','Jo�o')
INSERT INTO ##TABELA02 (ID,NOME) VALUES('2','Pedro')
SELECT * FROM ##TABELA02


---------------------------------------------------------------------
-- @ TABELAS QUE VALEM PARA O PROCEDIMENTO QUE ESTA SENDO EXECUTADO

DECLARE @LIMITE_MINIMO INT, @LIMITE_MAXIMO INT, @CONTADOR_NOTAS INT
DECLARE @TABELA_NUMEROS TABLE(NUMERO INT, [STATUS] VARCHAR (200))
CREATE TABLE #TABELA_NUMEROS2 (NUMERO INT, [STATUS] VARCHAR (200))

SET @LIMITE_MINIMO = 1
SET @LIMITE_MAXIMO = 1000

WHILE @LIMITE_MINIMO<=@LIMITE_MAXIMO
BEGIN
	SELECT @CONTADOR_NOTAS =  COUNT(*) FROM [NOTAS FISCAIS] WHERE NUMERO = @LIMITE_MINIMO
	IF @CONTADOR_NOTAS > 0
		BEGIN
			INSERT INTO  @TABELA_NUMEROS (NUMERO, [STATUS]) VALUES (@LIMITE_MINIMO, 'E NOTA FISCAL')
			INSERT INTO  #TABELA_NUMEROS2 (NUMERO, [STATUS]) VALUES (@LIMITE_MINIMO, 'E NOTA FISCAL')
		END
	ELSE
		BEGIN
			INSERT INTO  @TABELA_NUMEROS (NUMERO, [STATUS]) VALUES (@LIMITE_MINIMO, 'N�O E NOTA FISCAL')
			INSERT INTO  #TABELA_NUMEROS2 (NUMERO, [STATUS]) VALUES (@LIMITE_MINIMO, 'N�O E NOTA FISCAL')
		END
	SET @LIMITE_MINIMO = @LIMITE_MINIMO + 1
END

SELECT * FROM  @TABELA_NUMEROS
SELECT * FROM  #TABELA_NUMEROS2

