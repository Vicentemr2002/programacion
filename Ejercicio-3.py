# EJERCICIO 3

import random

lista = []

for i in range (0,78):
    numero = random.randint(1,1000)
    lista.append(numero)

lista.sort() 

print(lista)

print("el número menor es", lista[0])  

print("el número mayor es", lista[77]) 

for lista in range (0,78):
    if(lista% 2 == 0):
        print(lista)