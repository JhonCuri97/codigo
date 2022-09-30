#se pueden agregar o eliminar valores
dias=["lunes", "martes","miercoles", "jueves", "viernes", "sabado"]

print (dias)
#muestra desde la ps 1 al 4
print(dias[1:4])

#muestra longitud
print(len(dias))

#agrega una dto a la lista
dias.append("domingo")
print (dias)

#elimina el ultimo registro
dias.pop()
print(dias)

#elimian una dto en especifico
del dias[2]
print (dias)

#agregar valor en la posicion q quiero
dias.insert(3,"miercolessss")
print (dias)

for x in dias:
    print(x)