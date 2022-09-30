
print("Convertir de soles a dolares")
n1=float(input("ingrese el monto en soles "))

print("Ingrese la moneda a convertir: ")

tipomoneda=input()

if tipomoneda=="dolares":
    n2=4
elif tipomoneda=="euros":
    n2=2
else:
    n2=1
    
conversion=n1*n2
    
if conversion==n1:
    print("no se indico una moneda valida")
else:
    print("El resultado en soles es: " + str(conversion))   