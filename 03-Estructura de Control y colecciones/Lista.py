#-----------LISTAS---------------------

print("Datos 1")
datos=["felo", 33,"Robledo", True]
#Agregar datos a una lista
"""
Agrega un ítem al final de la lista. 
Equivale a a[len(a):] = [x].
"""
datos.append("INGENIERO DE SISTEMAS")
print(datos)

#extender datos a una lista
"""
Extiende la lista agregándole todos los ítems del iterable. 
Equivale a a[len(a):] = iterable.
"""

print("Datos 2")
datos2=["sura", "estrato 2","moto", True]
print(datos2)
print("Esto es una Lista extendida de Datos 1 y 2")
datos.extend(datos2)
print(datos)


#insertar datos en una lista en alguna posicion dada

"""
Inserta un ítem en una posición dada. El primer argumento
 es el índice del ítem delante del cual se insertará, por 
 lo tanto a.insert(0, x) inserta al principio de la lista y 
 a.insert(len(a), x) equivale a a.append(x).
"""
print("insertar datos en una lista en alguna posicion dada")
datos2.insert(2,"zmj47c")
print(datos2)