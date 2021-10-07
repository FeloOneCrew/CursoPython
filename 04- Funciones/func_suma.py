"""
Se indica la *args por convencion para indicar argumentos
indeterminados por posicion
"""

def sumar(*args):
    suma=0
    for n in args:
        suma +=n
    return suma

    print(args)

SumaTotal= sumar(1,2,3,4,5,6,7)
print("La suma  total es: ", SumaTotal)