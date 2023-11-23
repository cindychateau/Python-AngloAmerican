class Persona:

    #A través del método init INICIALIZAMOS o CREAMOS una nueva instancia
    #self va a incluir TODA la info de mi objeto individual
    #self = juana
    #nombre = "Juana"
    #apellido = "De Arco"
    #email = "juana@codingdojo.com"
    #juana.nombre = "Juana"
    #juana.apellido = "De Arco"
    #juana.email = "juana@codingdojo.com"
    #juana.lineas_codigo = 0
    def __init__(self, nombre, apellido, email, hobbies, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.lineas_codigo = 0 #lineas de codigo que han desarrollado
        self.edad = 18
        self.hobbies = hobbies
        self.mascota = mascota
        #self.mascota = Animal("gato", "Miu", "miau")
    
    #self - la instancia que está llamando al método
    def saludar(self):
        print(f'Te saluda {self.nombre}, ¡Hola!')
    
    #self = elena
    #cantidad_lineas = 20
    #elena.lineas_codigo = 10 + 20 = 30
    def codificar(self, cantidad_lineas):
        self.lineas_codigo += cantidad_lineas
    



