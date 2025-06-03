usuario = {
    "nombre": "Juan",
    "edad": 25,
    "lenguajes": ["Python", "JavaScript", "C++"]
}
import json
# escribir el diccionario en un archivo JSON
with open("usuario.json", "w", encoding="utf-8") as archivo:
    json.dump(usuario, archivo, indent=4)
# leer el diccionario del archivo JSON
with open("usuario.json", "r", encoding="utf-8") as archivo:
    usuario_leido = json.load(archivo)
    print(usuario_leido)  
print(usuario_leido["nombre"])  # Imprime el nombre del usuario
print(usuario_leido["lenguajes"])    # Imprime la lista de lenguajes del usuario