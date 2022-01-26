num = 1
def ePrimo(x):
    fator = 2
    while x % fator != 0 and fator < x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True
        

    
while num > 0 :
    num = int(input("Digite um número: "))
    if ePrimo(num):
        print("Este número é primo")
    else:
        print("Este número não é primo")

