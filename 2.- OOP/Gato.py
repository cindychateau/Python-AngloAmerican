from Animal import Animal
#class Hijo(Padre):
class Gato(Animal):

    def __init__(self, tipo, nombre, sonido, tipo_pelaje, raza):
        super().__init__(tipo, nombre, sonido)
        self.tipo_pelaje = tipo_pelaje
        self.raza = raza
    
    def razcar_sofa(self):
        print(f'{self.nombre} está razcando el sofá de su casa')