"""A. Sacar las fiestas del primer trimestre, almacenarlas 
en una lista y mostrarlas.
B. Imprime las fiestas de diciembre"""
#A

fiestas = {"enero":{1:"Año Nuevo", 6:"Reyes",31:"Cumpleaños Loreto"},
 "febrero": {14: "San Valentin"},
 "marzo": {19: "San José"},
 "abril":{17: "Jueves Santo",18:"Viernes Santo"},
 "mayo":{4:"Día de la madre"},
 "junio":{9: "Día de la Región de Murcia"},
 "julio":{6:"San Fermín"},
 "agosto":{15:"Asunción de la Virgen"},
 "septiembre":{16:"Romeria de la Fuensanta"},
 "octubre":{12:"El día del Pilar"},
 "noviembre":{1: "Día de todos los santos"},
 "diciembre":{6:"Día de la Constitución",8:"Día de la Inmaculada Concepción",24:"NocheBuena",25:"Navidad"}}

listatrimestral=[]
for mes in fiestas:
    if mes=="enero":
        listatrimestral.append(fiestas[mes])
        print (listatrimestral)
