import csv
datos = [
    ["Nombre", "Edad"],
    ["Juan", 25],
    ["María", 30],
    ["Pedro", 22],
]
# escribir los datos en un archivo CSV
# el archivo se crea en el directorio actual
with open("personas.csv", "w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerows(datos)
# leer los datos del archivo CSV
with open("personas.csv", "r", encoding="utf-8") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila)
