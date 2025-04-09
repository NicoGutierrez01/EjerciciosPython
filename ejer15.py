#Modifica el valor de una clave en el diccionario anterior (cambia edad)

def nombre (nombre = "Nico"):
    return nombre

def ciudad (ciudad = "Rafaela"):
    return ciudad

def edad(edad = 23):
    return edad

diccionario = {"nombre": nombre(), "ciudad": ciudad(), "edad": edad()}

diccionario["edad"] = 25

print(diccionario)
