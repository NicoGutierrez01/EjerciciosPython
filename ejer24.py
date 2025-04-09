# Define una clase Cuenta que encapsule el saldo y permita ingresar o retirar dinero.

class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def ingresar(self, cantidad):
        self.saldo += cantidad
        return self.saldo
    
    def retirar(self, cantidad):
        self.saldo -= cantidad
        return self.saldo
    
cuenta = Cuenta(0)

print(cuenta.saldo)

cuenta.ingresar(100)

print(cuenta.saldo)

cuenta.retirar(30)

print(cuenta.saldo)