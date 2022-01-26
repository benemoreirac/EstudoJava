def main():
    carro1 = Carro('brasilia', 1968, 'amarela', 80)
    carro2 = Carro('fusca', 1981, 'preto', 95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(self, modelo, ano, cor, velMaxima):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.vel = 0
        self.maxVelocidade = velMaxima

    def imprima(self):
        if self.vel == 0: #parado da para ver o ano
            print("%s %s %d"%(self.modelo, self.cor, self.ano))
        elif self.vel < self.maxVelocidade:
            print("%s %s indo a %d Km/h"%(self.modelo, self.cor, self.vel))
        else:
            print("%s %s indo muito rapido!"%(self.modelo, self.cor, self.maxVelocidade))

    def acelere(self, velocidade):
        self.vel = velocidade
        if self.vel >= self.maxVelocidade:
            self.vel = self.maxVelocidade
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()

main()
