#Crea dos funciones diferentes, cada una con una variable local llamada mensaje. Ejecuta ambas y muestra cómo no interfieren entre ellas.

def mensaje1():
    mensaje = "Mensaje de la funcion 1"
    print(mensaje)

def mensaje2():
    mensaje = "Mensaje de la funcion 2"
    print(mensaje)

mensaje1()
mensaje2()  

