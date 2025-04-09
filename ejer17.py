#Solicita números separados por comas y ordénalos de menor a mayor.

entrada = input("Numeros: ")

numeros = [int(x) for x in entrada.split(",")]

numeros.sort()

print("Ordenados:", numeros)