class Persona:

    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad
    

    def detalle_persona(self):
        print(f'Nombre: {self.nombre} \nedad: {self.edad}')

    def __str__(self): #Imprimir el estado de un objeto
        return f'Nombre: {self.nombre} \nedad: {self.edad}'


class Cliente (Persona):
    pass
