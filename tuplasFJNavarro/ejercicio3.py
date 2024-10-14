#Ejercicio 3:
#A. Crea una tupla con los números del 1 al 10.
num=[i for i in(range(1,11))]
numeros=(tuple(num))
print(numeros)
#B. Calcula la suma de todos los números.
total=sum(numeros) # Tambien se puede aplicar la formula (numeros[-1] * (numeros[-1]+1))/2
print (total)

