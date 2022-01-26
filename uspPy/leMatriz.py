def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" +str(i)+"][" + str(j)+"]"))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def leMatriz():
    lin = int(input('Digite o n de linhas da matriz: '))
    col = int(input('Digite o n de colunas da matriz: '))
    cria_matriz(lin,col)
    return cria_matriz(lin,col)
