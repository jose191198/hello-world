#Mi primer codigo de Data Rebels en python

nombre = "Jose Escobedo"
frase = "Uno siempre regresa a donde fue feliz"

respuesta = input("¿Quieres oir una frase inspiracional? (y/n)")

if respuesta == "n":
    print("No hay frase inspiracional")
elif respuesta == "y":
    print(f'{frase}, by {nombre}')