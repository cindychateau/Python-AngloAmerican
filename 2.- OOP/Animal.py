class Animal:

    def __init__(self, tipo, nombre, sonido):
        self.tipo = tipo
        self.nombre = nombre
        self.sonido = sonido
    
    def hacer_sonido(self):
        print(f'El/La {self.tipo} dice: {self.sonido}')