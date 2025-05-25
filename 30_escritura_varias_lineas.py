lineas = ["Primera linea\n","Segunda linea\n", "Tercera linea\n"]
with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas)  # Escribe varias líneas en el archivo
with open("notas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())