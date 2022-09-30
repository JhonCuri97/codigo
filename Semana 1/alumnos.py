#CRUD create, read,update,delte
#DEFINIR VARIABLES
alumnos=[]
alumno={}
salir='no'
#LOGICA

def createAlumno(nombre,correo,celular):
    nuevoAlumno={
            'nombre':nombre,
            'correo':correo,
            'celular':celular
        }
    alumnos.append(nuevoAlumno) 
    return 1

def readAlumno():
    print("LISTADO DE  alumnos")
    for a in alumnos:
            print("========================")
            for clave,valor in a.items():
                print(clave + ":" + valor)
                
def updateAlumno():
    print("Actualizar alumno")
    alumnoBuscar=input("Ingrese nombre del alumno : ")
    posA=-1
    for i in range(len(alumnos)):
        a=alumnos[i]
        for clave,valor in a.items():
            print("==================")
            if valor ==alumnoBuscar:
                print(a)
                posA=i
                print("Posicion del alumno"+str(posA))
    print("Actualizando alumnos")
    nombre=input("NOmbre: " )
    correo=input("Email: " )
    celular=input("Celular: ")
    nuevoAlumno={
            'nombre':nombre,
            'correo':correo,
            'celular':celular
        }
    del alumnos[posA]
    alumnos.insert(posA,nuevoAlumno)
                   
while(salir=='no'):
    print("OPCIONES : 1 - REGISTRAR ALUMNO 2 - MOSTRAR ALUMNOS 3  - ACTUALIZAR ALUMNO" )
    opcion=input("Ingrese opcion: ")    
    if(opcion=="1"):
        print("Registro de alumnos")
        nombre=input("NOmbre: " )
        correo=input("Email: " )
        celular=input("Celular: ")
        r= createAlumno(nombre,correo,celular) 
    
    elif (opcion =="2"):
        readAlumno()
        
    elif (opcion=="3"):
        updateAlumno()
    else:
        print("Opcion incorrecta")
        continue
    
    print("Desea salir del programa?")
    salir=input()
    
   
    
         
 
#RESULTADOS