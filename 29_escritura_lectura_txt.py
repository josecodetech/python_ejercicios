with open("saludo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, Mundo!\n")
    # archivo.close() no hace falta, el bloque with se encarga de cerrar el archivo
with open("saludo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)