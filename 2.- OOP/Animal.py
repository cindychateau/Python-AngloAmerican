class Animal:

    def __init__(self, tipo, nombre, sonido):
        self.tipo = tipo
        self.nombre = nombre
        self.sonido = sonido
    
    def hacer_sonido(self):
        print(f'El/La {self.tipo} dice: {self.sonido}')
    
    def comer(self):
        print(f'El animalito está comiendo')
    
    def ir_al_baño(self):
        raise NotImplementedError