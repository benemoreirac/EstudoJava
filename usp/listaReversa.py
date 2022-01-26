num = 1
lista = []
listaReversa = []
indice = 0

while num != 0:
    num = int(input("Digite um numero inteiro: "))
    if num != 0:
        lista.append(num)

tamanho = len(lista)

while tamanho > 0:
    listaReversa.append(lista[tamanho-1])
    tamanho = tamanho -1

print("Lista Principal: ", lista)
print("Lista Reversa: ", listaReversa)
