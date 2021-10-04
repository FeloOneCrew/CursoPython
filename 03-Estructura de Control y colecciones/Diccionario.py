"""
Los diccionarios se encuentran a veces en otros lenguajes 
como «memorias asociativas» o «arreglos asociativos». A diferencia
 de las secuencias, que se indexan mediante un rango numérico, 
 los diccionarios se indexan con claves, que pueden ser cualquier
  tipo inmutable; las cadenas y números siempre pueden ser claves. 
  Las tuplas pueden usarse como claves si solamente contienen cadenas,
números o tuplas; si una tupla contiene cualquier objeto mutable 
directa o indirectamente, no puede usarse como clave. No podés usar 
listas como claves, ya que las listas pueden modificarse usando 
asignación por índice, asignación por sección, o métodos como 
append() y extend().

Es mejor pensar en un diccionario como un conjunto de pares 
clave:valor con el requerimiento de que las claves sean únicas 
(dentro de un diccionario). Un par de llaves crean un diccionario 
vacío: {}. Colocar una lista de pares clave:valor separada por comas
 dentro de las llaves agrega, de inicio, pares clave:valor al 
 diccionario; esta es, también, la forma en que los diccionarios 
 se muestran en la salida.

"""

numeros = {'uno':1 ,'dos':2 ,'tres':3 , 'cuatro':4 , 'cinco':5 }
print(numeros)

numeros['seis'] = 6 # Añadir un nuevo elemento al diccionario
print(numeros)
print(numeros['tres'])

