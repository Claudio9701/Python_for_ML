#%%
'''1'''
# Tenemos una lista, imprime la suma para cada uno de los valores en la posicion i e i+1
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]

#%%
'''solucion 1'''

for i in range(len(lista1)-1):
    suma = lista1[i] + lista1[i + 1]
    print(suma)
    
#%%
'''2'''
# Arma una nueva lista con los rsultados de la multiplicacion de cada valor en la lista a
# con cada valor de la lista b

a_list = [1, 2, 3, 4, 5]
b_list = [10, 20, 30, 40, 50]

#%%
'''solucion 2'''

a_b_list = []
for a in a_list:
    for b in b_list:
        mult = a*b
        a_b_list.append(mult)

print(a_b_list)

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
'''solucion 3'''

def velocidad_final(lista_objeto):
    tiempo = lista_objeto[0]
    unidad = lista_objeto[1]
    
    if unidad == "segundos":
        tiempo_segundos = tiempo
    elif unidad == "minutos":
        tiempo_segundos = tiempo*60
    elif unidad == "horas":
        tiempo_segundos = tiempo*60*60
    
    velocidad_final = 9.18*tiempo_segundos
    return velocidad_final

velocidad_1 = velocidad_final(objeto_1)
velocidad_2 = velocidad_final(objeto_2)    
velocidad_3 = velocidad_final(objeto_3)    

print(velocidad_1, velocidad_2, velocidad_3)

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
'''solucion 4'''
dict_nuevos_sueldos = {}
def nuevo_sueldo(lista_empleados):
    
    for empleado in lista_empleados:
        
        nombre = empleado[0]
        titulo = empleado[1]
        antiguedad = empleado[2]
        subordinados = empleado[3]
        
        if titulo==0:
            dict_temp = {nombre: 1000}
            dict_nuevos_sueldos.update(dict_temp)
            
        elif antiguedad<=2 and subordinados==0:
            dict_temp = {nombre: 2200}
            dict_nuevos_sueldos.update(dict_temp)
            
        elif antiguedad>2 and subordinados==0:
            dict_temp = {nombre: 3500}
            dict_nuevos_sueldos.update(dict_temp)
            
        elif subordinados>0 and subordinados<=10:
            dict_temp = {nombre: 5000}
            dict_nuevos_sueldos.update(dict_temp)
            
        elif subordinados>10:
            dict_temp = {nombre: 8000}
            dict_nuevos_sueldos.update(dict_temp)
    
    return dict_nuevos_sueldos
            
    
dict_nuevos_sueldos = nuevo_sueldo(empleados)
print(dict_nuevos_sueldos)

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

def max_residuo_de_max_mult(lista1, lista2, lista3):
    max_1 = max(lista_a)
    max_2 = max(lista_b)
    max_mult = max_1*max_2
    
    max_res = 0
    for i in lista3:
        res = max_mult%i
        
        if res > max_res:
            max_res = res
            val_3 = i
    
    return [max_1, max_2, val_3, max_res]

vals_max_res = max_residuo_de_max_mult(lista_a, lista_b, lista_c)
print(vals_max_res)        
    
#%%
'''Para mas ejercicios de programacion'''
# https://projecteuler.net/archives
# https://www.hackerrank.com/
