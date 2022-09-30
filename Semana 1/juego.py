#Juego
from random import choice

print("seleccione una opcion: ")
jugador= input()
computadora=""
resultado=""

jugadas=["piedra","papel","tijera"]
computadora=choice(jugadas)
print("la pc escogió: " + computadora)

#for x in jugadas:
 #   if jugador==jugadas:
  #      resultado ="empate"
    

if jugador=="piedra":
    if computadora=="piedra":
        resultado="empate"
    elif computadora=="papel":
        resultado="computadora"
    elif computadora=="tijera":
        resultado="jugador"
        
elif jugador=="papel":
    if computadora=="piedra":
        resultado="jugador"
    elif computadora=="papel":
        resultado="empate"
    elif computadora=="tijera":
        resultado="computadora"  
        
elif jugador=="tijera":
    if computadora=="piedra":
        resultado="computadora"
    elif computadora=="papel":
        resultado="jugador"
    elif computadora=="tijera":
        resultado="empate"  
        
print("El ganador es: " + resultado)   
