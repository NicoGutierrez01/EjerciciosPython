#Verifica si una palabra ingresada es palíndromo utilizando listas.

palabra = input("Ingrese una palabra: ")

palabras = palabra.split()

if palabras == palabras[::-1]:
    print("La palabra es palíndromo")
else:
    print("La palabra no es palíndromo")