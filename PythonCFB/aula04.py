"""
Tipos basicos em python

"""
x = 1
print("O valor: " + str(x))
print("O tipo: "+str(type(x)))
print()

y = "CFB"
print("O valor: " + str(y))
print("O tipo: "+str(type(y)))
print()

z = 1.0
print("O valor: " + str(z))
print("O tipo: "+str(type(z)))
print()

b = True
print("O valor: " + str(b))
print("O tipo: "+str(type(b)))
print()

l = ["Carro", "Avião", "Navio"] #lista
print("O valor: " + l[0])
print("O tipo: "+str(type(l)))
print()

t = ("Carro", "Avião", "Navio") #tupla
print("O valor: " + t[0])
print("O tipo: "+str(type(t)))
print()

r = range(0,100,1) #Lista
print("O valor: " + str(r[0]))
print("O tipo: "+str(type(r)))
print()

d = { #dict
    "canal": "CFB Cursos",
    "curso": "Curso de Pyrhon",
    "nome": "bene"
} 
print("VAlor: "+d["canal"])
print("O Tipo: "+ str(type(d)))
print()

s = {5,7,4,7,4,8} #set
print("Valor: "+str(s))
print("Tipo" + str(type(s)))
print()
