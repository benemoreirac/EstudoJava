quantidade = int(input("Digite a quantidade de valores que gostaria de Multiplicar: "))

produto = 1
i = 1

while i <= quantidade:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    i = i + 1

print("A soma dos valores é: ", produto)
