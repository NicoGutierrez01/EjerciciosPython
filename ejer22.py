#Define una clase Coche con método arrancar() que devuelva un mensaje.

class Coche:
    def __init__(self,marca):
        self.marca = marca

    def arrancar(self):
        return f"El auto {self.marca} ha arrancado"

mi_auto = Coche("Toyota")

print(mi_auto.marca)
print(mi_auto.arrancar())

