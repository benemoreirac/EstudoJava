

def MinMax(temperaturas):
    print("A menor temperatura do mes foi: ", minima(temperaturas), "C")
    print("A maior temperatura do mes foi: ", maxima(temperaturas), "C")

def minima(temps):
    min = temps[0]
    i = 0
    while i<len(temps):
        if temps[i] < min:
            min = temps [i]
        i = i+1
    return min

def maxima(temps):
    max = temps[0]
    i = 0
    while i<len(temps):
        if temps[i] < max:
            max = temps [i]
        i = i+1
    return max

def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para Lista", temp)
        print("O valor esperado era: ", valor_esperado, ". Valor calculado: ", valor_calculado)
    
def testa_minima():
    print("Iniciando os testes!")
    teste_pontual([0], 0)
    teste_pontual([0,0,0,0,0], 0)
    teste_pontual([0,1,2,3,4,5,6,7,8,9,10], 0)
    print("Testes Finalizados")
   
    
    
    
