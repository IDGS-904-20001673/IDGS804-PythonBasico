#son parecidas a los arreglos

lista1=["Roberto",1.2,23,True]
print(lista1)
print(lista1[:])
print(lista1[2:4])
print(lista1[:2])
print(lista1[3:])

lista1.append("leonel")
print(lista1)
lista1.insert(0,"Mario")
print(lista1)
lista1.extend([9,10,11])
print(lista1)

print(lista1.index("leonel"))#te dice en que posicion esta el elemento que buscas

lista1.remove("Roberto")
print(lista1)
lista1.pop()
print(lista1)