"""La profesora de informática quiere crear un programa para organizar la clase:
Partiendo de la lista de nombres de los alumnos de la clase, los situe en la disposición de las
mesas de la clase que tiene forma de matriz 3x4 de manera aleatoria. (3 filas, 4 columnas)
Por ejemplos: La lista tiene 12 nombres, sale un nombre aleatorio de la lista, y en la primera
posición de la matriz, la posición (0,0) se situe ese nombre.
Nota: Una forma común de construir matrices es haciendo uso de listas anidadas (o listas de
listas). Si una lista convencional forma un vector de elementos, al hacer que cada elemento sea
un vector, se obtiene una matriz de elementos.
Para crear una matriz vacía se puede utilizar listas de comprensión:
matriz_alumnos = [[0 for _ in range(4)] for _ in range(3)]
"""
import random
def elejir(lista):
    alumno=random.choice(lista)
    return alumno
def borrar(alumno,lista):
    lista.remove(alumno)

alumnos=["Juan Peres","Francisco Paez","Antonia Zamora",
         "Perico palotes","juanita reina","Alfonso Garcia",
         "Menganito Poe","Fulanita jauja","Enrique Jimenez",
         "Ana Gonzalez","Isabel lueve","Paquito rocero"]
matriz_alumnos = [[0 for _ in range(4)] for _ in range(3)]
for a in range(len(matriz_alumnos)):
    for b in range(len(matriz_alumnos[a])):
        al=elejir(alumnos)
        matriz_alumnos[a][b]=al
        borrar(al,alumnos)
for a in range(len(matriz_alumnos)):
    print (matriz_alumnos[a])
