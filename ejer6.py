#Solicita tres números y muestra cuál es el mayor.

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

if n1 > n2 and n1 > n3:
    print("El mayor es el primer número")
elif n2 > n1 and n2 > n3:
    print("El mayor es el segundo número")
else:    
    print("El mayor es el tercer número")