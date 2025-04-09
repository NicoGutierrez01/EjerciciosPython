#Crea una clase base Animal con método hacer_sonido() y dos clases derivadas Perro y Gato que sobrescriban este método.

class Animal:
    def hacer_sonido(self):
        return "Sonido generico"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"
    
mi_perro = Perro()
mi_gato = Gato()

print(mi_perro.hacer_sonido())
print(mi_gato.hacer_sonido())
    
