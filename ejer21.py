#Crea una clase Persona con atributos nombre y edad, e instancia un objeto.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Nico", 23)


print(persona1.nombre)
print(persona1.edad)
