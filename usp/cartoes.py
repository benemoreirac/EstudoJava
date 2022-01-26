meuCartao = int(input("Digite o num do CC: "))

cartaoLido = 1
encontreiMeuCartaoNaLista = False

while cartaoLido != 0 and not encontreiMeuCartaoNaLista:
    cartaoLido = int(input("Digite o numero do proximo CC: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNaLista = True

if encontreiMeuCartaoNaLista:
    print("Meu CC esta na lista!")
else:
    print("Cartão não encontrado na Lista!")
