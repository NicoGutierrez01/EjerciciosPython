#Cuenta cuántas palabras tiene una oración dada por el usuario usando listas.

oracion = input("Oracion: ")

palabras = oracion.split()

cantidad = len(palabras)

print("La oración tiene", cantidad, "palabras")