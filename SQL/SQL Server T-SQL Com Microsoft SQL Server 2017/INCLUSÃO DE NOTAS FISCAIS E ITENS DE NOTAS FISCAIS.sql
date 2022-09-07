/** AULA GERA DADOS NOTA FISCAL **/
DECLARE @CLIENTE VARCHAR(12)
DECLARE @VENDEDOR VARCHAR(12)
DECLARE @PRODUTO VARCHAR(12)
DECLARE @DATA DATE
DECLARE @NUMERO INT
DECLARE @IMPOSTO FLOAT
DECLARE @NUM_ITENS INT
DECLARE @CONTADOR INT
DECLARE @QUANTIDADE INT
DECLARE @PRECO FLOAT

SET @DATA = FORMAT(GETDATE(),'dd/MM/yyyy')
SET @CLIENTE = [dbo].[EntidadeAleatoria]('CLIENTE')
SET @VENDEDOR = [dbo].[EntidadeAleatoria]('VENDEDOR')
SELECT @NUMERO = MAX(NUMERO) + 1 FROM [NOTAS FISCAIS]
SET @IMPOSTO = 0.18
SET @CONTADOR = 1
SET @NUM_ITENS = [dbo].[NumeroAleatorio](2,10)

PRINT 'CABE�ARIO'
PRINT @DATA
PRINT @CLIENTE
PRINT @VENDEDOR
PRINT @IMPOSTO
PRINT @NUMERO

PRINT 'ITENS'
WHILE @CONTADOR <= @NUM_ITENS
BEGIN	
	SET @PRODUTO = [dbo].[EntidadeAleatoria]('PRODUTO')
	SET @QUANTIDADE = [dbo].[NumeroAleatorio](5,100)
	SELECT @PRECO = [PRE�O DE LISTA] FROM [TABELA DE PRODUTOS] WHERE [CODIGO DO PRODUTO] = @PRODUTO
	PRINT @NUMERO
	PRINT @PRODUTO
	PRINT @QUANTIDADE
	PRINT @PRECO
	PRINT '-----'
	SET @CONTADOR = @CONTADOR + 1
END


/** EXERC�CIO INSERE DADOS NOTA FISCAL **/
DECLARE @CLIENTE VARCHAR(12)
DECLARE @VENDEDOR VARCHAR(12)
DECLARE @PRODUTO VARCHAR(12)
DECLARE @DATA DATE
DECLARE @NUMERO INT
DECLARE @IMPOSTO FLOAT
DECLARE @NUM_ITENS INT
DECLARE @CONTADOR INT
DECLARE @QUANTIDADE INT
DECLARE @PRECO FLOAT
DECLARE @LISTA_PRODUTOS TABLE (PRODUTO VARCHAR(20))
DECLARE @AUX_PRODUTO INT

SET @DATA = FORMAT(GETDATE(),'dd/MM/yyyy')
SET @CLIENTE = [dbo].[EntidadeAleatoria]('CLIENTE')
SET @VENDEDOR = [dbo].[EntidadeAleatoria]('VENDEDOR')
SELECT @NUMERO = MAX(NUMERO) + 1 FROM [NOTAS FISCAIS]
SET @IMPOSTO = 0.18
SET @CONTADOR = 1
SET @NUM_ITENS = [dbo].[NumeroAleatorio](2,10)

INSERT INTO [NOTAS FISCAIS] (CPF, MATRICULA, DATA, NUMERO, IMPOSTO)
VALUES(@CLIENTE, @VENDEDOR, @DATA, @NUMERO, @IMPOSTO)

WHILE @CONTADOR <= @NUM_ITENS
BEGIN	
	SET @PRODUTO = [dbo].[EntidadeAleatoria]('PRODUTO')
	SELECT @AUX_PRODUTO = COUNT(*) FROM @LISTA_PRODUTOS WHERE PRODUTO = @PRODUTO
	IF @AUX_PRODUTO = 0
	BEGIN
		SET @QUANTIDADE = [dbo].[NumeroAleatorio](5,100)
		SELECT @PRECO = [PRE�O DE LISTA] FROM [TABELA DE PRODUTOS] WHERE [CODIGO DO PRODUTO] = @PRODUTO
		INSERT INTO [ITENS NOTAS FISCAIS] (NUMERO, [CODIGO DO PRODUTO], QUANTIDADE, PRE�O)
		VALUES(@NUMERO, @PRODUTO, @QUANTIDADE, @PRECO)
		SET @CONTADOR = @CONTADOR + 1
	END
	INSERT INTO @LISTA_PRODUTOS (PRODUTO) VALUES(@PRODUTO)
END