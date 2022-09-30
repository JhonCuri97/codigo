class vehiculo:
    
    def __init__(self,mar,km,col):
        self.marca=mar
        self.kilometraje=km
        self.color=col
    
    def encender(self):
        print("Encendiendo.....")
        
    

class auto (vehiculo):
    def __init__(self,mar,km,col,cap):
        super().__init__(mar,km,col)
        self.capacidad=cap
    
    def encender(self):
        super().encender()
        print("auto.......")
        
class camion(vehiculo):
    def __init__(self,mar,km,col,ej):
        super().__init__(mar,km,col)
        self.eje=ej
        
    def encender(self):
        super().encender()
        print("camion")

ferrari = auto('ferrari','100','azul','2')
ferrari.encender()    

volvo = camion('volvo','100','verde','8')
volvo.encender()    