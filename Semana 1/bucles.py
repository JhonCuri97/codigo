n=int (input("ingrese tabla de multiplicar: "))
for x in range(1,12):
    tabla=n*x
    print(str(n) + " multiplicado por " + str(x) + "=" + str(tabla))
    

i=1
while i<12:
    tabla= n*i
    print(str(n) + " multiplicado por " + str(i) + "=" + str(tabla))
    i+=1