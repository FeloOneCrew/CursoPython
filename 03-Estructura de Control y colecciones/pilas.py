#-----utilizar una lista como Pila
"""
Los métodos de lista hacen que resulte muy fácil usar 
una lista como una pila, donde el último elemento añadido
 es el primer elemento retirado («último en entrar, primero en salir»). Para agregar un elemento a la cima de la pila, utiliza append(). Para retirar un elemento de la cima de la pila, utiliza pop() sin un índice explícito.
"""

print("Esto es una Pila")
datos=[1, 2, 3, 4, 5 , 6 , 7, 8]
print(datos)
p=0
y= int(len(datos))
while p < y:
    datos.pop()
    print(datos)
    p+=1