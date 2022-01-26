import math

class Bhaskara:
    
    def delta(self,a, b, c):
        return b**2-4*a*c

    def main():
        a = int(input("Digite um valor para A: "))
        b = int(input("Digite um valor para B: "))
        c = int(input("Digite um valor para C: "))
        print(self.calcula_raizes(a,b,c))

    def calcula_raizes(self, a, b, c):
        d = self.delta(a, b, c)
        if d == 0:
            raiz1 = ((-b)+ math.sqrt((b**2)-(4*a*c)))/(2*a)
            return 1, raiz1
        else:
            if d < 0:
                return 0
            else:
                x1 = ((-b)+ math.sqrt((b**2)-(4*a*c)))/(2*a)
                x2 = ((-b)- math.sqrt((b**2)-(4*a*c)))/(2*a)
                return 2, raiz1, raiz2









