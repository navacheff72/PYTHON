"""Ejercicio 6: 
 A. Crea una tupla anidada para representar una pequeña biblioteca. Cada elemento de la tupla 
 será un libro con título, autor y año de publicación. 
 • Cien años de soledad, Gabriel García Márquez, 1967 
 • El señor de los anillos, J.R.R. Tolkien, 1954 
 • La sombra del viento, Carlos Ruiz Zafón, 2001 
 • Orgullo y prejuicio, Jane Austen, 1813 
 • 1984, George Orwell, 1949 
 • Harry Potter y las Reliquias de la Muerte, J.K. Rowling, 2007 
 • Ángeles y demonios, Dan Brown, 2000 """

libros=(("Cien años de soledad","Gabriel García Márquez",1967),("El señor de los anillos",
        "J.R.R. Tolkien",1954),("La sombra del viento","Carlos Ruiz Zafón",2001),("Orgullo y prejuicio",
        "Jane Austen",1813),("1984","George Orwell",1949),("Harry Potter y las Reliquias de la Muerte",
        "J.K. Rowling",2007),("Ángeles y demonios","Dan Brown",2000))
print (libros)
# B.  Imprime todos los libros publicados después de 2000 
num=len(libros)
for i in range(num) :
    if (libros[i][2]) > 2000 :
        print (libros[i])
# ¿Porque no deja poner  la tupla como range del for a modo de lista ? 
