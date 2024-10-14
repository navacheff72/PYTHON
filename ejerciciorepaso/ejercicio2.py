"""Ejercicio 2.
A. Crea una función que muestra una tabla de multiplicar.
B. Modifica ese programa para que imprima las tablas de
 multiplicar del 1 al 10. Se puede hacer con funciones."""
#A
def tabla(a):
    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")
tabla(2)
#B
for x in range (1,11):
    tabla(x)
