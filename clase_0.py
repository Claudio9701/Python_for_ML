# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 00:56:15 2019

@author: USUARIO
"""
#%%
#una variable es un espacio de memoria en el que Python guarda algún valor
x=5
y="hola"
a,b=1,2
#%%
#print es una funcion de Python que nos permite visualizar variables y mucho mas
print(x)
print (y)
print(a)
print(b)
print (y+" mundo")
#como vemos, juntar palabras en Python es tan facil como sumarlas
#%%
#una lista es una variable que contiene varios valores
lista=[1,2,"tres",4,5]
print(lista)
#%%
#las variables no solo almacenan un valor, sino tambien un "tipo"
print(type(x))
print(type(y))
print(type(lista))
print(type(5.5))
#es importante saber de que tipo es tu variable
#%%
#ahora veamos como funciona la mate (integers)
print(2+2)
print(2*2)
print(50-5*6)
print(50/10)
print(2**3) #doble multiplicacion es elevado a
#%%
#sigamos con un poco mas de mate
division=20/3
print(division)

division_exacta=20//3
print(division_exacta)

residuo=20%3
print(residuo)

print(division_exacta*3+residuo)
#estos operadores especiales pueden ser muy utiles
#%%
#resolucion al problema 1
donacion=1635*0.2
niños=donacion//60
print(niños)

#%%
#ahora algo sobre palabras (string)
palabra="esternocleidomastoideo"
print(palabra)
print(palabra[0]) #primera letra
print(palabra[6]) #sexta letra
print(palabra[-1]) #ultima letra
print(palabra[-2]) #penultima letra

print(palabra[0:2]) #letras de la posición 0 (incluida) a la posición 2 (excluida)
print (palabra[2:-1]) #letras de la posición 2 (incluida) a la posición 8 (excluida)

print(palabra[:5]) #letras desde el inicio hasta la posición 5 (excluida)
print(palabra[6:]) #letras desde la posicion 6 hasta el final
print(palabra[-3:]) #letras desde la antepenultima posicion hasta el final
print(palabra[:-2]) #letras desde el inicio hasta la penultima posicion (excluida)

print(len(palabra))
#%%
#subamosle el nivel con listas (lists)
lista1=[1,2,3,4,5]
lista2=[1,4,9,17,25]

print(lista1[0]) #primer elemento de la lista
print(lista2[-1]) #ultimo elemento de la lista
print(lista2[:4]) #desde el elemento en la posicion 2 de la lista hasta el final

print(lista2[1]/lista1[1]) #dividimos dos elementos de las listas
print(lista1+lista2) #las listas sumadas crean una nueva lista con todos los elementos

#%%
#mas listas
lista2[3]=16 #asiganamos el valor 16 al elemento en la posicion 3
print(lista2)

lista2.append(36) #agregamos el valor 36 a la lista
print(lista2)

lista1[3:]=["se me dio la gana de cambiar esto","y escribir lo que queria"] #cambiamos los valores de la posicion 3 en adelante
print(lista1)

lista1[3:]=[] #borramos los valores de la posicion 3 en adelante
print(lista1)

print(len(lista1))

#%%
#aun mas listas
lista3=[lista1,lista2]
print(lista3)
print(len(lista3))
print(len(lista3[0]))
#la lista 3 es una lista de listas

print(lista3[0]) #su primer elemento es la lista1 completa

print("el primer elemento del primer elemento de mi lista 3 es: ",lista3[0][0])
#aca seleccionamos el primer elemento del primer elemento de la lista3

#%%
#conozcamos la funcion if
lista1=[1,2,3,4,5]
lista2=[1,4,9,16,25]

if lista1[0]==1: 
   print("verdad") #el igual en condiciones debe usar doble signo

#else es la respuesta que da si no se cumple la condicion
if lista1[0] > lista2[3]:
    print ("verdad")
else:
    print ("mentira")

#otra forma de escribir lo mismo
a = "verdad" if lista1[0] > lista2[3] else "mentira"
print(a)

#elif sirve para dar varias condiciones escalonadas, si no cumple una, pasa a la siguiente
if lista1[1] >= lista2[1]:
    print ("verdad 1")
elif lista1[len(lista1)-1] != lista2[1]:
    print("verdad 2") #el simbolo != en Python significa "diferente"

#otra forma de escribir lo mismo
print ("verdad 1") if lista1[1] >= lista2[1] else print("verdad 2") if lista1[len(lista1)-1] != lista2[1] else print ("mentira")
#esta forma necesita terminar con un else si o si

#%%
#un poco mas de if

#'and' sirve para pedir que dos o mas condiciones se cumplan a la vez
if lista1[0]==1 and lista2[0]==1: print("verdad")
else: print("mentira")

#'or' sirve para pedir que al menos una condicion se cumpla
if lista1[0]==1 or lista2[1]==1: print("verdad")
else: print("mentira")

#%%
#ahora vamos con los for

lista1=[1,2,3,4,5]
lista2=[1,4,9,16,25]
#en estas lineas hacemos que el for recorra nuestra lista1. A esto se le llama iterar
for i in lista1:
    print (i) #la separacion antes del print se llama indentacion, es porque print pertenece a la funcion for
#%%
for x in "hola": print (x) #for tambien recorre strings
#%%
for i in lista2:
    print(i)
    if i==16: print("4 al cuadrado") #las funciones que van dentro del for se repiten por cada iteracion
    else: print("no estoy buscando este numero")
    
#%%
#otro tipo de for

for i in range(5): #i toma los valor del 0 al 5-1
    print (i)
else: print("listo!") #else en for se activa una vez que termina
#%%  
print("\n") #asi se imprime un enter en python
for i in range (5,10): #i toma valores del 5 al 10-1
    print(i)
#%%
print("\n") #asi se imprime un enter en python
for i in range (1,10,2): print(i)  #i toma los valor del 1 al 10-1 avanzando de 2 en 2

#%%
#mas for

for i in lista1: #i toma el valor de todos los elementos en la lista1
    for j in lista2: #por cada valor que toma i, j toma el valor de todos los elementos en la lista2
        print(i,j)

print("\n")
for i in range(len(lista1)):
    print(lista1[i], lista2[i])

print("\n")
for i in lista1:
    print(i)
    if i==3: break #break hace que el for se termine si comple la condicion

print("\n")
for i in lista1:
    if i==3: break #el orden de los factores si altera el producto en este caso
    print(i)
    
print("\n")
for i in lista1:
    if i<3:
        continue #continue hace que i salte al siguiente valor si cumple la condicion
    print (i)
