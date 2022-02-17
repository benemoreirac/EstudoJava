#String que será digitada
senha = input("Digite a Senha desejada: ")

#criação de listas com as condições para senha
#cb = caixaBaixa, cA = caixaAlta, dig = digito, carE = caractere Especial
cB, cA, dig, carE = 0, 0, 0, 0
caracteres = "!@#$%^&*()-+"

#função para validação das condições
def validaSenha(senha, caracteres, cB, cA, dig, carE):
    print(senha)
    if len(senha)==6:
        for caracter in senha:
            if (caracter.islower()):
                cB +=1
            if (caracter.isupper()):
                cA +=1
            if (caracter.isdigit()):
                dig +=1
            if (caracter in caracteres):
                carE +=1
    if (cB>=1 and cA>=1 and dig>=1 and carE>=1 and cB+cA+dig+carE==len(senha)): 
        print("Senha Valida") 
    else: 
        print("Senha invalida")
        novaSenha = input("Digite uma nova Senha (Ou 'exit' para sair!): ")
        if ('exit' not in novaSenha):
            validaSenha(novaSenha, caracteres, cB,cA, dig, carE)
            

#chamada da função
validaSenha(senha, caracteres, cB,cA, dig, carE)
print("Fim do programa")