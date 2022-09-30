
class Rectangulo:
    
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
    
    def area(self):
        return self.ancho*self.alto
    
class Cuadrado:
    
    def __init__(self,lado):
        self.lado=lado
        
    def area(self):
        return self.lado ** 2
    
class Figurageometrica(Rectangulo,Cuadrado):
    def __init__(self, tipo, ancho, alto):
        self.tipo=tipo
        Rectangulo.__init__(self,ancho,alto)
        Cuadrado.__init__(self,ancho)
        
    def area(self):
        if self.tipo=="Rectangulo":
            return Rectangulo.area(self)

        else:
            return Cuadrado.area(self)
        

c= Figurageometrica("Cuadrado",20,30)
area=c.area()
print(area)

r=Figurageometrica("Rectangulo",20,30)
area=r.area()
print(area)
