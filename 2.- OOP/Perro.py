from Animal import Animal
class Perro(Animal):

    def __init__(self, tipo, nombre, sonido, raza, años):
        super().__init__(tipo, nombre, sonido)
        self.raza = raza
        self.años = años
    
    def perseguir_autos(self):
        print(f'{self.nombre} está persiguiendo un auto!')
    
    def ir_al_baño(self):
        print(f'Sale a pasear, va al baño y su dueño recoge los desechos')