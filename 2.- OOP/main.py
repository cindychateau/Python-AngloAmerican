#Importación de la clase
from Persona import Persona
from Animal import Animal

miu = Animal("gato", "Miusita", "miau")
michi = Animal("gato", "Michigan", "purrr")
firulais = Animal("perro", "Firulais", "guau")

elena = Persona("Elena", "De Troya", "elena@codingdojo.com", ["Leer", "Estudiar", "Jugar"], michi) #instancia = objeto inicializado
juana = Persona("Juana", "De Arco", "juana@codingdojo.com", ["Bailar", "Hacer ejercicio"], miu)

elena_saenz = Persona("Elena", "Saenz", "elen@codingdojo.la", ["Tocar el piano"], firulais)

print(elena.nombre)
print(juana.nombre)
print(elena_saenz.apellido)

elena.saludar()
juana.saludar()

elena.codificar(10) 
juana.codificar(3)
elena.codificar(20)
print(elena.lineas_codigo)





miu.hacer_sonido()
michi.hacer_sonido()


firulais.hacer_sonido()

print(elena.mascota.nombre)

# elena.mascota.nombre = "Pelusa"
# elena.mascota.tipo = "vaquita"
# elena.mascota.sonido = "muuuuu"
elena.mascota.hacer_sonido()