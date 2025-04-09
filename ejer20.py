#Solicita un número y devuelve los números primos desde 1 hasta dicho número.

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))

primos = [i for i in range(1, numero + 1) if es_primo(i)]

print("Pirmos: ", primos)