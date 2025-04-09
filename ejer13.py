#Crea una función que devuelva la cantidad de vocales en una cadena.

def cantidad_vocales(cadena):
    vocales = 0
    for letra in cadena:
        if letra.lower() in "aeiou":
            vocales += 1
    return vocales    

cadena = input("Ingrese una cadena: ")    
print("La cantidad de vocales es:", cantidad_vocales(cadena))