
#inputs
alumnos=[]
alumno={}
salir='no'

#desarrollo

while (salir=='no'):
    print("OPCIONES: 1)Registrar alumnos        2)Ver alumnos")
    opcion=input()
    if opcion=="1":
        nombre= input("Ingrese el nombre del alumno: ")
        email= input("Ingrese el email del alumno: ")
        celular= input("ingrese el celular del alumno: ")
        nuevo={
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        alumnos.append(nuevo)
        
    elif opcion=="2":
        
        for a in alumnos:
            for clave,valor in a.items():
                print(clave + ":" + valor)
    
    else:
        print("Opcion incorrecta")
        salir= input() 