#Enunciado: Programa que permite al usuario adivinar un número generado al azar dando pistas si es mayor o menor.
# El usuario adivina correctamente tras varias pistas.

import random
numero_secreto = random.randint(1, 100)

print("🔢 Adivina el número (entre 1 y 100)")

intento = None  # Inicializamos la variable

while intento != numero_secreto:
    intento = int(input("Tu intento: "))
    
    if intento < numero_secreto:
        print("📈 Es más alto")
    elif intento > numero_secreto:
        print("📉 Es más bajo")
    else:
        print("🎉 ¡Correcto! El número era", numero_secreto)