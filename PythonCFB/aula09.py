carros = ["HRV","Golf","Argo","Focus"]
print(carros[0])

carros[3] = "Fusca"
print(carros)

carros.append("Fit")
carros.append("Logus")
carros.append("Polo")
carros.append("Fox")
print(carros)

print(str(len(carros))+" Carros na lista") 
carros2 = list(carros)

carros.remove("Fit")
carros.pop()
print(carros)

del carros[2]
print(carros)

carros.clear()
print(carros)

print(carros2)

carros3 = carros+carros2
print(carros3)