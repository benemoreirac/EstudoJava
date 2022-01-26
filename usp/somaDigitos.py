numero = int(input("Digite um numero inteiro com mais de um digito: "))

soma= 0

while numero!= 0:
    resto = numero % 10
    soma = soma + resto    
    numero = numero // 10
    
print("Soma é:", soma)
