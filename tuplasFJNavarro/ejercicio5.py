#Ejercicio 5: 
# A. Crea una lista de números. 
lista=[i for i in range(1,11)]
print (lista)
# B. Convierte la lista en una tupla. 
tupla=(tuple(lista))
print (tupla)
# C. Multiplica cada elemento de la tupla por 2 y guarda el resultado en una nueva tupla. 
lista=(i*2 for i in lista)
tupla2=(tuple(lista))
print (tupla2)
