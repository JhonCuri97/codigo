#la tupla es estatica

dias=("lunes", "martes","miercoles", "jueves", "viernes", "sabado")
primos=(2,3,5,7,11,13)

print(dias)
print(max(primos))

#convertor tupla a lista
primos2=list(primos)
primos2.pop()
primos=tuple(primos2)
