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
resultado_suma2 = sumatoriaReturn(6, 7)
resultado_suma3 = sumatoriaReturn(0, 3)
print("El resultado es:",resultado_suma)

#Función que reciba un arreglo y que regrese la suma de los valores del arreglo
#arr = [4, 5, 6, 7]
#suma = 0
#num = 4
#suma = 0 + 4 = 4
#num = 5
#suma = 4 + 5 = 9
#num = 6
#suma = 9 + 6 = 15
#num = 7
#suma = 15 + 7 = 22
def sumatoria_arreglo(arr):
    suma = 0
    for num in arr:
        suma += num
    return suma

def sumatoria_arreglo2(arr):
    return sum(arr)

print(sumatoria_arreglo([4, 5, 6, 7]))
print(sumatoria_arreglo2([4, 5, 6, 7]))

#Función que reciba un arreglo y que regrese el número mayor del arreglo
def numero_mayor(arr):
    num_mayor = arr[0]
    for num in arr:
        if num_mayor < num:
            num_mayor = num

    return num_mayor

def numero_mayor2(arr):
    return max(arr)

print(numero_mayor([2, 8, 4, 9]))
print(numero_mayor2([2, 8, 4, 9]))

#Función que reciba un arreglo y reciba un número y regrese True si el número se encuentra dentro del arreglo o False si NO se encuentra en el arreglo
def existe_numero(arr, num):
    for x in arr:
        if x == num:
            return True
    return False


print(existe_numero([1, 2, 3], 3))
print(existe_numero([1, 2, 3], 4))


#Parámetro por Default -> En dado caso de que algún argumento no se envíe, mi parámetro funcionara por default
def hello(nombre="Elena", apellido="De Troya"):
    print(f"¡Hola {nombre} {apellido} !")
    #print("¡Hola "+nombre+" "+apellido+"!")
    

hello()
hello("Juana")
hello("Juana", "De Arco")

hello(apellido="De Arco")

#num1 = 4, num2 = 1
#num1 = 4, num2 = 5
#num = 1, num2 = 1
def multiplacion(num1=1, num2=1):
    return num1*num2


print(multiplacion(4))
print(multiplacion(4, 5))
print(multiplacion())