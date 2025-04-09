#Crea una clase Calculadora que inicialice con dos números y tenga métodos para sumar y restar.

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2 

    def restar(self):
        return self.num1 - self.num2 

mi_calculadora = Calculadora(10, 5)

print(mi_calculadora.sumar())
print(mi_calculadora.restar())