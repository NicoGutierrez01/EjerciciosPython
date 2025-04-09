# Crea una función que genere los primeros 'n' números Fibonacci.
#resultado esperados Términos: 5
#0, 1, 1, 2, 3

def fibonacci(n):
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

# Pedir al usuario la cantidad de términos
terminos = int(input("Términos: "))

# Mostrar la secuencia
resultado = fibonacci(terminos)
print(", ".join(str(num) for num in resultado))