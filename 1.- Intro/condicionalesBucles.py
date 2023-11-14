#Para ejecutar en MAC: python3 nombre_archivo.py
#Para ejecutar en Windows: py nombre_archivo.py O python nombre_archivo.py
# CONDICIONALES
x = 20
if x > 10:
    print("El número ingresado es mayor a 10")
    print("El número es:",x)
else:
    print("El número es menor a 10")


edad_infante = 4
if edad_infante < 2:
    print("El infante es un bebe")
elif edad_infante < 5:
    print("El infante es un toddler")
else:
    print("El infante es un niño")


temperatura = 20
estaLloviendo = False
if temperatura > 18 and not estaLloviendo:
    print("Salgamos al parque")

edad = 17
permisoPadres = True
if edad > 18 or permisoPadres:
    print("Puedes tener tu licencia de manejo")


# BUCLES
for x in range(5): #Rango del 0-4. 5 YA NO entra
    print(x)

print("-------")

for y in range(5, 12): #(Comienzo, Fin) -> Fin no entremos. 5-11
    print(y)

print("-------")

for z in range(2, 12, 2): #(Comienzo, Fin, Paso). 2-11 avanzando de 2 en 2
    print(z)

# RECORRER UN ARREGLO
lista_nombres = ["Elena", "Juana", "Pablo", "Pedro"]

#for(let i=0; i<lista_nombres.length; i++)
for i in range(len(lista_nombres)): #0-3 len(arreglo) = tamaño de mi lista
    print("Posición:",i,"Valor:",lista_nombres[i])

#nombre = "Elena"
#nombre = "Juana"
#nombre = "Pablo"
#nombre = "Pedro"
for nombre in lista_nombres:
    print(nombre)

estudiante = {
    "nombre": "Elena",
    "apellido": "De Troya",
    "edad": 19
}

#llave = "nombre"
#llave = "apellido"
#llave = "edad"
for llave in estudiante:
    print(llave, estudiante[llave])

print(llave)

inicio = 0
final = 5
while inicio < final:
    print("Inicio:",inicio,"Final:",final)
    inicio += 1
    final -= 1
else:
    print("Se terminó de cumplir. Inicio:",inicio,"Fin:",final)

# BREAK -> interrumpir por completo mi ciclo/bucle
for x in range(16):
    if x == 13:
        break
    print(x)

# CONTINUE -> interrupcion temporal. SOLO no ejecuta en la ronda correspondiente
for x in range(16):
    if x == 13:
        continue
    print(x)

texto = "Buen dia"
for caracter in texto:
    print(caracter)


#RETO INDIVIDUAL
#Dado el for 1 al 15, imprime todos los numeros EXCEPTO aquellos múltiples de 5


#Dada una cadena, imprima cada uno de los caracteres y que se detenga POR COMPLETO si encuentra un . (PUNTO)
cadena = "Hola, buenos dias. Como estas"




