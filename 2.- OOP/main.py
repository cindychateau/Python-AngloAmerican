#Importación de la clase
from Persona import Persona

elena = Persona("Elena", "De Troya", "elena@codingdojo.com", ["Leer", "Estudiar", "Jugar"]) #instancia = objeto inicializado
juana = Persona("Juana", "De Arco", "juana@codingdojo.com", ["Bailar", "Hacer ejercicio"])

elena_saenz = Persona("Elena", "Saenz", "elen@codingdojo.la", ["Tocar el piano"])

print(elena.nombre)
print(juana.nombre)
print(elena_saenz.apellido)

elena.saludar()
juana.saludar()

elena.codificar(10) 
juana.codificar(3)
elena.codificar(20)
print(elena.lineas_codigo)