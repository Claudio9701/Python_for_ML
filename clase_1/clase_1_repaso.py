#%%
'''1'''
# Tenemos una lista, imprime la suma para cada uno de los valores en la posicion i e i+1
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]

#%%
    
#%%
'''2'''
# Arma una nueva lista con los rsultados de la multiplicacion de cada valor en la lista a
# con cada valor de la lista b

a_list = [1, 2, 3, 4, 5]
b_list = [10, 20, 30, 40, 50]

#%%

#%%
'''3'''
# Cuando un objeto esta en caida libre acelera a razon de 9.18 metros por segundo
# Desarrolle un funcion que tome como input una lista con el formato
# [tiempo de caida, unidad de tiempo de caida (segundos, minutos u horas)]
# y de como output la velocidad final del objeto
# Pruebe la funcion con los 3 ejemplos provistos

objeto_1 = [10, "segundos"]
objeto_2 = [5, "minutos"]
objeto_3 = [2, "horas"]

#%%

#%%
'''4'''
# El Coronavirus ha obligado a las empresas a ajustar sus costos. Para Ripley, el costo mas importante es el de planilla.
# Por ello, han decidido ajustar a todos sus empleados administrativos a 5 bandas salariales:

# Trainee (1000 soles): todos los empleados que no tengan titulo universitario
# Analista JR (2200 soles): todos los empleados que tengan 2 años o menos en la empresa y nadie a su cargo
# Analista SR (3500 soles): todos los empleados que tengan mas de 2 años en la empresa y nadie a su cargo
# Lider JR (5000 soles): todos los empleados que tengan hasta 10 personas a su cargo
# Lider SR (8000 soles): todos los empleados que tengan mas de 10 personas a su cargo

# Desarrolle una funcion que tome como input una lista de empleados con listas del formato
# [nombre del empleado, titulo universitario (si=1, no=0), tiempo en la empresa, personas a su cargo]
# Y devuelva como output un diccionario con el formato
# {nombre de la persona: nuevo sueldo}
# Tome la lista empleados como ejemplo

empleados = [["Juan", 0, 2, 0],
             ["Monica", 1, 10, 30],
             ["Roberto", 0, 1, 0],
             ["Martin", 1, 5, 5],
             ["Rosa", 1, 1, 0],
             ["Maria", 1, 6, 12],
             ["Gabriela", 1, 3, 2],
             ["Rodrigo", 1, 3, 0],
             ["Jose", 1, 20, 6],
             ["Gonzalo", 1, 5, 10]]

#%%

#%%
'''5'''
# Desarrolle una funcion que tome como input 3 listas son numeros y
# encuentre el mayor valor entre la multiplicacion de los valores de la lista 1 y la lista 2
# encuentre el mayor residuo de la division entre este resultado y los valores de la tercera lista
# devuelva una lista con el formato
# [valor de primera lista utilizado, valor de segunda lista utilizado, valor de tercera lista utilizado, residuo resultante]
# utilice las listas provistas como ejemplo
# tip: utilice la funcion max de Python

lista_a = [4, 5, 12, 6, 17, 4]
lista_b = [3, 4, 7, 1, 7, 9]
lista_c = [2, 5, 4, 7, 2, 8]

#%%

#%%
'''Para mas ejercicios de programacion'''
# https://projecteuler.net/archives
# https://www.hackerrank.com/
