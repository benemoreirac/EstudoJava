lista_principal = []
lista_clone = []
dado = 1


def clone(lista):
    for item in lista:
        lista_clone.append(item)
    return lista_clone        
    

while dado != 0:
    dado = int(input("Digite um dado ou 0 para sair: "))
    if dado != 0:
        lista_principal.append(dado)

clone_correto = lista_principal[:]


print("Lista Principal: ", lista_principal)
print("Lista Clone: ", clone(lista_principal))

print("Clone correto: ", clone_correto)

print(" 3 listas COncatenadas", lista_principal + clone_correto )

del clone_correto[1:4]

print("Lista excluida: 1:4 ", clone_correto)



