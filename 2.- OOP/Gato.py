from Animal import Animal
#class Hijo(Padre):
class Gato(Animal):

    def __init__(self, tipo, nombre, sonido, tipo_pelaje, raza):
        super().__init__(tipo, nombre, sonido)
        self.tipo_pelaje = tipo_pelaje
        self.raza = raza
    
    def razcar_sofa(self):
        print(f'{self.nombre} está razcando el sofá de su casa')

    #Sobreescritura/Anulación
    def hacer_sonido(self):
        print(f'El gato te ve un momento, se aleja de ti y después dice: {self.sonido}')
    
    def ir_al_baño(self):
        print(f'Va a su caja, razca la arena y va al baño')