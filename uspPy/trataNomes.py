nome = "zero"
lista = []

while nome != "sair":
    print("Digite um nome  Lista")
    nome = input(":")
    if nome != "sair":
        lista.append(nome.strip().capitalize())
        
def trata_nomes(lista):
    maisCurto = ""
    count = 0
    for item in lista:
        count = len(item)
        maisCurto = item
        if count > len(maisCurto):
            maisCurto = item

    return maisCurto
            
    

print(trata_nomes(lista))
    
