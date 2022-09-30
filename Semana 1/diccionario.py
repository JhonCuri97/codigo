

capitales={'Peru':'Lima','Chile':'Santiago','Ecuador':'QUito','Brasil':'Braisilia'}

print(capitales['Peru'])

#Agregar al diccionario
capital={'EEUU':"Washington"}
capitales.update(capital)
print(capitales)


alumnos={
    'nombre':'JHon',
    'correo':'asd@gmail,com',
    'celular':'12345'
}
print(alumnos['correo'])
alumnos['correo']='ccc@gmail.com'
print(alumnos['correo'])

print(capitales.keys())   #peru chile...
print(capitales.values())   #lima santiago...

#recorrer diccionario
for clave in capitales:
    print(clave,alumnos[clave])
    
for clave,valor in alumnos.items():
    print(clave,valor)