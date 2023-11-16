#def = define -> Definiendo una función
def saludo():
    print("¡Hola Mundo!")

#nombre = "Juana"
def saludoNombre(nombre):
    print(f"¡Hola {nombre}!")

#num1 = 5, num2 = 6
def sumatoria(num1, num2):
    print(num1+num2)

#num1 = 8, num2 = 9
def sumatoriaReturn(num1, num2):
    return num1+num2

saludo()
saludoNombre("Elena")
saludoNombre("Juana")
sumatoria(5, 6)

resultado_suma = sumatoriaReturn(8, 9) #resultado_suma = 17
print("El resultado es:",resultado_suma)

#Función que reciba un arreglo y que regrese la suma de los valores del arreglo

#Función que reciba un arreglo y que regrese el número mayor del arreglo

#Función que reciba un arreglo y reciba un número y regrese True si el número se encuentra dentro del arreglo o False si NO se encuentra en el arreglo



