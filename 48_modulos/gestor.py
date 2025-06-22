import json
import os
from modelo import Usuario

class GestorUsuarios:
    def __init__(self, archivo):
        self.archivo = archivo
        self.usuarios = self.cargar()
    def cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Usuario(**d) for d in datos]
        return []
    def guardar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump([u.to_dict() for u in self.usuarios], f, indent=4)
    def crear_usuario(self, nombre, email):
        self.usuarios.append(Usuario(nombre,email))
        self.guardar()
    def listar(self):
        for i, u in enumerate(self.usuarios, 1):
            print(f"{i}. {u.nombre} - {u.email}")
    def actualizar(self, indice, nombre, email):
        if 0 <= indice < len(self.usuarios):
            self.usuarios[indice].nombre = nombre
            self.usuarios[indice].email = email
            self.guardar()
    def eliminar(self, indice):
        if 0 <= indice < len(self.usuarios):
            del self.usuarios[indice]
            self.guardar()