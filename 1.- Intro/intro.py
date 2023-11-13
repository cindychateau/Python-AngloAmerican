#Para ejecutar en MAC: python3 nombre_archivo.py
#Para ejecutar en Windows: py nombre_archivo O python nombre_archivo.py
print("Hola mundo")

#Booleans
boolean = True #True o False

#Numerales
num = 10 #enteros SIN DECIMALES
fl = 10.99 # flotantes CON DECIMALES
#parseInt() 
nuevo_float = float(10) #Forzo a un número entero que se convierta en flotante
print(nuevo_float)
nuevo_entero = int(fl) #Forzo a número flotante que se convierta en entero
print(nuevo_entero)
print(round(fl)) #round(numero) me permite redondear

import random #Importamos librería random
num_aleatorio = random.randint(2, 5) #Número entero aleatorio entre 2 y 5
print(num_aleatorio)

#Cadenas/Textos/Strings
string = "ABCDEFG"
nombre = "Juana"
apodo = "juanita"
print('Este es el alfabeto', string) #La coma en automático me agrega un espacio
print("Este es el alfabeto "+string) #el + concatena las cadenas tal cual están
print("Este es un numero", 10)
#print("Este es un numero"+ 10) #ERROR -> cree que el + va a sumar
print("Este es un numero"+ str(10)) 
print(f"Este es el alfabeto {string}!")
print(f"Les presenta a {nombre}, le pueden llamar '{apodo}' ")

#Métodos de manipulación de cadenas
string2 = "hola mundo! soy Juana de Arco y hoy en 13 de Noviembre"
print(string2.title()) #Primera letra de cada palabra debe ser mayúscula
print(string2.upper()) #Todo en mayúscula
print(string2.lower()) #Todo en minúscula
print(string2.count('oy')) #Regresa cuántos 'oy' hay en la cadena

string3 = "Elena!Juana!Pablo!Pedro"
print(string3.split('!')) #Enlista y divide mi cadena en base al caracter dado
print(string2.find('juana')) #Devolver dónde comienza 'Juana. Regresa -1 si no encuentra. Case-sensitive

#Tuplas. MUY parecido a una lista PERO no pueden cambiar de valor
tupla1 = ("Elena", "Juana", "Pedro", "Pablo") #Paréntesis para tupla
print(tupla1[0])
#tupla1[0] = "Elenita" -> ERROR la tupla NO puede ser cambiada
tupla2 = ("Texto", 7, 10.3, False) #Puedo tener distintos tipos de datos

#Listas / Array / Arreglo
lista_vacia = [] #array vacío
lista_nombres = ["Hugo", "Paco", "Luis"] #0-> Hugo, 1-> "Paco", 2-> "Luis"
print(lista_nombres[2])
lista_nombres[2] = "Donald"
print(lista_nombres)
lista_nombres.pop() #Elimina la última posición de mi lista
print(lista_nombres)
lista_nombres.pop(0) #Elimina la posición indicada
print(lista_nombres)
lista_nombres.append("Mickey") #Se agrega elemento al final de la lista
print(lista_nombres)

lista_mix = ["texto1", 11, True, 1.1, ["lista1", "lista2"]]
nueva_lista = lista_mix + lista_nombres
nueva_lista.append("Otro elemento")
print(nueva_lista)

#Diccionarios (Objetos en Javascript)
diccionario_vacio = {}
estudiante = {
    "nombre": "Juana",
    "apellido": "De Arco",
    "edad": 18,
    "soltera": True,
    "hobbies": ["leer", "comer", "salir al parque"]
}

print(estudiante["nombre"])
estudiante["edad"] = 19
print(estudiante)
estudiante["estatura"] = 1.67
print(estudiante)
estudiante.pop("soltera")
print(estudiante)

diccionario_vacio['total_gastado'] = 100
diccionario_vacio['lista_compras'] = ["verdura", "cereal"]

lista_alumnos = [
    {"nombre": "Elena", "apellido": "De Troya", "id": 123, "cursos": ["Fundamentos de la Web", "Python"]},
    {"nombre": "Juana", "apellido": "De Arco", "id": 234, "cursos": ["Fundamentos de la Web", "Python", "MERN"]},
    {"nombre": "Pedro", "apellido": "Páramo", "id": 345, "cursos": ["Fundamentos de la Web", "Python", "MERN", "Java"]}
]

#¿Cómo eliminamos de la lista de cursos MERN para Pedro?