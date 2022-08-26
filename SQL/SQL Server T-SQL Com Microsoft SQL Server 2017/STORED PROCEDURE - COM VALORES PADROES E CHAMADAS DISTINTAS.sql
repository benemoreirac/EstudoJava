/*PROCEDURE COM VALORES PADROES*/
CREATE PROCEDURE BuscaNotasCliente
@CPF AS VARCHAR(12),
@DATA_INICIAL AS DATETIME = '20160101',
@DATA_FINAL AS DATETIME = '20161231'
AS 
BEGIN
	SELECT * FROM [NOTAS FISCAIS] WHERE CPF = @CPF AND [DATA] BETWEEN @DATA_INICIAL AND @DATA_FINAL
END

EXEC BuscaNotasCliente @CPF='19290992743'
EXEC BuscaNotasCliente @CPF='19290992743', @DATA_INICIAL='20161201'
EXEC BuscaNotasCliente @CPF='19290992743', @DATA_FINAL='20160131'--n√O IMPORTA A ORDEM
EXEC BuscaNotasCliente '19290992743' /*sera considerada primeira variavel declarada*/
/*utilizando o DEFAULT n„o precisa passar parametro, que aceitara o parametro iniciado */