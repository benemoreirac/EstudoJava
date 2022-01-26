opc = 1
n1 = n2 = 0

while opc != 0:
    numero = int(input("Digite o numero para verificação: "))
    n1 = numero % 10
    numero = numero // 10
    n2 = numero % 10

    if n1 == n2:
        print("São Adjacentes ",n1, " e ",n2)
    else:
        numero = numero // 10
        n2 = numero % 10       

    opc = int(input("Para sair digite 0 ! Para continuar Digite 1!  "))
    
