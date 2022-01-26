import ordenador
import random
import time

class ContaTempos:
    def lista_aleatoria(self,n):
        lista = [0 for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(1000)
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = ordenador.Ordernador()
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("bolha demorou: ", depois-antes , " segundos")

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecao direta: ", depois-antes,  " segundos")
        
