num = int(input("Digite um numero inteiro >1: "))
fator = 2
multiplicidade = 0

while num > 1:
    while num % fator == 0:
        multiplicidade = multiplicidade + 1
        num = num / fator
    if multiplicidade > 0:
        print("fator ", fator, "multiplicidade ", multiplicidade)
    fator = fator + 1
    multiplicidade = 0
