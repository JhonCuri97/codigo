#PRONEDIO DE NOTAS

notas=[]
totalNotas= int(input("Cuantas notas desea evaluar: "))
promedio=0

for n in range(1, totalNotas +1):
    nota=int(input("nota " + str(n) + ":"))
    promedio += nota
    notas.append(nota)

promedio= promedio/totalNotas
    
print(notas)
print(min(notas))
print(max(notas))
print(promedio)

