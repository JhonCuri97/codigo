f= open('alumnos.txt','a')
print("Registro alumno: ")
nombre= input("NOmbre: ")
correo=input("correo: ")
celular=input("celular: ")

f.write('\n' + nombre + "," + correo + "," + celular)
f.close()

fr=open('alumnos.txt', 'r')
alumno=fr.read()
print(alumno)
fr.close

#a añadir  valores
#r solo leer
# """ comentar varias lineasz
