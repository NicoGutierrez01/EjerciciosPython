#Calcula el factorial de un número entero positivo.

numero = int(input("Ingrese un número entero positivo: "))

factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(factorial)