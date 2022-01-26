import matriz

def multiplica_matriz(A,B):
    num_linhas_A, num_colunas_A = len(A), len(B[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    assert num_colunas_A == num_linhas_B

    c = []
    for linha in range(num_linhas_A):
        #comecando uma nova linha
        C.append([])
        for coluna in range(num_colunas_B):
            #adcionando uma nova coluna na linha matriz B
            C[linha].append(0)
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][k]*B[K][coluna] 
if __name__ == "__main__":
    A = [[1,2,3],[4,5,6]]
    B = [[1,2],[3,4], [4,6]]
    print(multiplica_matriz(A,B))
