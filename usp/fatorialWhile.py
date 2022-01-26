def fatorial(num):
    fatorial = 1
    while num > 1:
        fatorial = fatorial * num
        num = num - 1
    return fatorial

num = int(input(" Digite um numero inteiro: "))
while num > 0:    
    print(fatorial(num))
    num = int(input(" Digite um numero inteiro: "))


    
    
