#Operção de casting, tipos numericos.
import random

num_i = 10
num_f = 5.2
num_c = 1j

x = num_i
y = num_f
z = num_c
num_random = random.randrange(0,59)

print("Valor: " + str(x) + " - Tipo: " + str(type(x)))
print("Valor: " + str(y) + " - Tipo: " + str(type(y)))
print("Valor: " + str(z) + " - Tipo: " + str(type(z)))
print("Valor: " + str(num_random) + " - Tipo: " + str(type(num_random)))
