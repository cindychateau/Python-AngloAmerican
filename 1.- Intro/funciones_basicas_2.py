'''
Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como posicion 0) hasta 0 (como último elemento). 
'''
def cuenta_regresiva(num):
    lista = []
    for x in range(num, -1, -1):
        lista.append(x)
    return lista

print(cuenta_regresiva(5))

'''
Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
'''
#lista = [1, 2]
def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]

print("Retorno:",imprimir_y_devolver([1, 2]))

'''
Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
'''
def primero_mas_longitud(lista):
    return lista[0] + len(lista)

print(primero_mas_longitud([1,2,3,4,5]))

'''
SI - Valores mayores que el segundo: escribe una función que acepte una lista y 
SI - cree una nueva 
SI - que contenga solo los valores de la lista original que sean mayores que su segundo valor. 
SI - Imprime cuántos valores son y luego 
devuelve la lista nueva. 
SI - Si la lista tiene menos de 2 elementos, has que la función devuelva False
'''
def valores_mayores_que_el_segundo(lista_recibida):
    lista_regresada = []
    if len(lista_recibida) < 2:
        return False
    else :
        #Comparar todos los elementos con lista_recibida[1]
        for x in lista_recibida:
            if x > lista_recibida[1]:
                lista_regresada.append(x)
        print(len(lista_regresada))
        return lista_regresada

print("Regresa:",valores_mayores_que_el_segundo([5,2,3,2,1,4]))

'''
Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
'''
def longitud_valor(tamano, valor):
    lista = []
    #range(fin) - 0 - uno antes de fin -> range(5) 0, 1, 2, 3, 4
    #for(let i=0; i<tamano; i++)
    #tamano = 4
    #0, 1, 2, 3
    #i = 0
    #lista = [7]
    #i = 1
    #lista = [7, 7]
    #i = 2
    #lista = [7, 7, 7]
    #i = 3
    #lista = [7, 7, 7, 7]
    for i in range(tamano):
        lista.append(valor)
    return lista

print(longitud_valor(4, 7))
print(longitud_valor(6, 2))