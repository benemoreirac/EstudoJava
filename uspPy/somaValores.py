quantidade = int(input("Digite a quantidade de valores que gostaria de somar: "))

soma = 0
i = 1

while i <= quantidade:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor
    i = i + 1

print("A soma dos valores é: ", soma)
