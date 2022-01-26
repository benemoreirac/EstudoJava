decrescente = True
anterior = int(input("Digite o primeiro número da sequência: "))

valor = 1

while valor!= 0 and decrescente:
    valor = int(input("Digite um numero da sequencia: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente == True:
    print("A Sequencia está em ordem decresnte!")
else:
    print("A sequencia não é decrescente!")
