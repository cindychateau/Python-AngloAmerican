from Animal import Animal
class Perro(Animal):

    def __init__(self, tipo, nombre, sonido, raza, años):
        super().__init__(tipo, nombre, sonido)
        self.raza = raza
        self.años = años
    
    def perseguir_autos(self):
        print(f'{self.nombre} está persiguiendo un auto!')