# Define funciones independientes para suma, resta, multiplicación y división. Usa una de ellas con dos números.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def división(a, b):
    return a / b

calcu = input("Ingrese la función a usar (suma= 1, resta=2, multiplicación=3 o división=3): ")

if calcu == "1":
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    print("La suma es:", suma(a, b))
elif calcu == "2":
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    print("La resta es:", resta(a, b))
elif calcu == "3":
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    print("La multiplicación es:", multiplicacion(a, b))
elif calcu == "4":
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    print("La división es:", división(a, b))
else:
    print("Opción no válida")
   