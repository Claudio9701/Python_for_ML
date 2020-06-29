#%%
'''1'''
# Tenemos una lista, imprime cada uno de los valores uno a uno
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]

#%%

#%%
'''2'''
# Tenemos dos listas, compara los valores en una misma posición en ambas listas e imprime
# "a" si el valor de la lista a es mayor y "b" si el valor de la lista b es mayor

a = [1, 4, 6, 2, 10, 12]
b = [2, 3, 5, 6, 2, 14]

#%%
   
#%%
'''3'''
# Para las mismas listas del ejericio anterior, compara los valores de la lista a
# con los valores de la lista b e imprime "si" si el valor en una posicion i de la lista a
# es mayor al valor en una posicion i-1 de la lista b, caso contrario imprime "no"

#%%

#%%
'''4'''
# Para las mismas listas del ejercicio anterior, imprime la suma y la division entre los valores
# en una misma posicion de las listas a y b

#%%

#%%
'''5'''
# Para cada valor en la lista x, imprima la suma con cada valor de la lista y
x_list = [1, 2, 3, 4, 5, 6]
y_list = [7, 8, 9, 10]

#%%
      
#%%
'''6'''
# Para cada elemento en la lista, imprime el elemento si es de tipo string
lista_combinada = [0, 1, 2, "tres", 4, 5, "6", 7, "ocho"]

#%%

#%%
'''7'''
# Para cada elemento de la lista del ejercicio anterior, si el elemento es de tipo string
# cambialo por el elemento de tipo integer correspondiente

#%%

#%%
'''8'''
# Para cada elemento de la lista, si el elemento es par, imprime "par"
# caso contrario, imprime "impar"

lista_par_impar = [1, 2, 4, 7, 9, 15, 21, 37, 40, 51, 99, 101, 514, 617]

#%%

#%%
'''9'''
# Para la lista anterior, crea una nueva lista solo con los valores pares

#%%

#%%
'''¿Como va todo hasta aca?'''

#%%
'''Definicion de funciones'''
# Conocemos como definir funciones propias en Python

#%%
''' ejemplo 1 '''
#Funcion que suma dos numeros
def suma (a, b):
    suma = a + b
    return suma

suma_1_2 = suma(1, 2)
print(suma_1_2)

#%%
'''ejemplo 2'''
#Funcion que devuelve la resta absluta de dos numeros
def resta_absoluta (x, y):
    if x>y:
        resta = x-y
        return resta
    else:
        resta = y-x
        return resta

resta_absoluta_5_10 = resta_absoluta(5, 10)
resta_absoluta_10_5 = resta_absoluta(10, 5)

print(resta_absoluta_5_10, resta_absoluta_10_5)

#%%
'''ejemplo 3'''
# Funcion que elimina el valor minimo de una lista (sin usar la funcion min)
def eliminar_valor_minimo (lista):
    minimo = lista[0]
    i_min = 0
    for i in range(1, len(lista)):
        if i < minimo:
            minimo = lista[i]
            i_min = i
    
    lista.pop(i_min)
    return lista

r = [9, 2, 5, 7, 10, 3, 15]
r = eliminar_valor_minimo(r)
print(r)
r = eliminar_valor_minimo(r)
print(r)

#%%
'''ejemplo 4'''
# Funcion que crea una nueva lista con los valores de una lista que se encuentren en otra segunda lista
def lista_interseccion (lista1, lista2):
    lista3 = []
    for i1 in lista1:
        if i1 in lista2:
            lista3.append(i1)
    
    return lista3

lista1 = [1, 3, 5, 7, 9, 11, 13, 15]
lista2 = [3, 5, 7, 11, 13]
lista3 = lista_interseccion(lista1, lista2)
print(lista3)

#%%
'''De vuelta a los ejercicios'''
#%%
'''10'''
# El banco de la Nación se encuentra en búsqueda de automatizar procesos y
# le piden ayuda con el proceso de crédito. Los niveles de crédito son los siguientes:
# Nivel 1 (10%): El cliente lleva al menos 5 años de antiguedad, tiene trabajo y su score crediticio es A o B
# Nivel 2 (15%): El cliente tiene trabajo y su score crediticio es A o B
# Nivel 3 (20%): El cliente lleva al menos 2.5 años y o no tiene trabajo o su score crediticio es C
# Denegado: En cualquier otro caso el credito es denegado
# Desarrolle una funcion que tenga como input la antiguedad del cliente, si tiene trabajo (1 si, 0 no)
# y su score crediticio y el output sea el nivel de credito correspondiente

#%%
'''solucion 10'''

#%%
'''Una pausa para conocer los diccionarios'''
#%%
diccionario_ejemplo = {"uno": 1,
                       "dos": 2,
                       "tres": 3}

print(diccionario_ejemplo.keys())
print(diccionario_ejemplo.values())
print(diccionario_ejemplo["uno"])

print("\n")
for i in diccionario_ejemplo:
    print(i, "-->", diccionario_ejemplo[i])
#%%
diccionario_ejemplo_2 = dict(uno=1, dos=2, tres=3)

print(diccionario_ejemplo_2.keys())
print(diccionario_ejemplo_2.values())
print(diccionario_ejemplo_2["uno"])

print("\n")
for i in diccionario_ejemplo_2:
    print(i, "-->", diccionario_ejemplo_2[i])
#%%
'''De vuelta a los ejercicios'''
#%%
'''11'''
# La inmobiliaria Imagina necesita mejorar su proceso de valoracion de inmuebles.
# La valoracion de inmuebles es igual a los metros cuadrados * el valor por metro cuadrado segun la zona
# Desarrolle una funcion que tenga como input una lista de cualquier tamaño que contenga listas del formato:
# [nombre del departamento, metros cuadrado, zona]
# Y tenga como output un diccionario del formato: {nombre del departamento: valor}, pruebela con la lista de ejemplo

diccionario_zona_valorm2 = {1: 800,
                            2: 1000,
                            3: 1200,
                            4: 1500}

inmuebles = [["Inm 1", 100, 2],
            ["Inm 2", 80, 3],
            ["Inm 3", 150, 1],
            ["Inm 4", 75, 2],
            ["Inm 5", 110, 4],
            ]

#%%

#%%
'''12'''
#Crea una lista con los 1000 primeros numeros primos

#%%
