"""A. Crear un programa que imprima los 10 primeros 
números naturales utilizando tanto un bucle while como el
 bucle for.
B. Modificar el programa anterior para que muestre 10
 números aleatorios entre 1 y 50 (modulo random) realizar
 la modificación tanto para el bucle while, como el bucle
 for.
C. Crear 2 listas, una para números pares y otra impares.
 Rellenar esas listas con los números aleatorios del
 apartado B.
D. Con las listas impares, crear una lista y añadir los 
números que sean múltiplos de 3.
E. Con las listas pares, crear otra lista con los números
 menores a 25.
F. Imprimir por pantalla ambas listas."""
#A
c=0
while c<10:
    c=c+1
    print (c)
for c in range(10):
    print (c+1)
#B
import random
c=0
while c<10:
    c=c+1
    print (random.randint(1,50))
for c in range(10):
    print (random.randint(1,50))
#C
impares=[]
pares=[]
c=0
while c<10:
    c=c+1
    n=random.randint(1,50)
    if n%2==0 :
        pares.append(n)
    else:
        impares.append(n)
print(f" numeros pares: {pares}")
print(f" numeros impares: {impares}")
impares=[]
pares=[]
for c in range(10):
    n=random.randint(1,50)
    if n%2==0 :
        pares.append(n)
    else:
        impares.append(n)
print(f" numeros pares: {pares}")
print(f" numeros impares: {impares}")
#D
impares=[]
pares=[]
c=0
while c<10:
    c=c+1
    n=random.randint(1,50)
    if n%2==0 :
        pares.append(n)
    else:
        impares.append(n)
imparesmult3=[]
for i in impares :
    if i%3==0 :
        imparesmult3.append(i)
print(f" numeros pares: {pares}")
print(f" numeros impares: {impares}")
print(f" Numeros impares multiplos de 3: {imparesmult3}")
impares=[]
pares=[]
for c in range(10):
    n=random.randint(1,50)
    if n%2==0 :
        pares.append(n)
    else:
        impares.append(n)
imparesmult3=[]
for i in impares :
    if i%3==0 :
        imparesmult3.append(i)
print(f" numeros pares: {pares}")
print(f" numeros impares: {impares}")
print(f" Numeros impares multiplos de 3: {imparesmult3}")
#E
impares=[]
pares=[]
c=0
while c<10:
    c=c+1
    n=random.randint(1,50)
    if n%2==0 :
        pares.append(n)
    else:
        impares.append(n)
imparesmult3=[]
for i in impares :
    if i%3==0 :
        imparesmult3.append(i)
paresinferiores=[]
for i in pares:
    if i<25 :
        paresinferiores.append(i)
print(f" numeros pares: {pares}")
print(f" numeros pares inferiores a 25: {paresinferiores}")
print(f" numeros impares: {impares}")
print(f" Numeros impares multiplos de 3: {imparesmult3}")
impares=[]
pares=[]
for c in range(10):
    n=random.randint(1,50)
    if n%2==0 :
        pares.append(n)
    else:
        impares.append(n)
imparesmult3=[]
for i in impares :
    if i%3==0 :
        imparesmult3.append(i)
paresinferiores=[]
for i in pares:
    if i<25:
        paresinferiores.append(i)
print(f" numeros pares: {pares}")
print(f" numeros pares inferiores a 25: {paresinferiores}")
print(f" numeros impares: {impares}")
print(f" Numeros impares multiplos de 3: {imparesmult3}")

