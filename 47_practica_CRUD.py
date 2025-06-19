import json
import os
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'email': self.email
        }
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
gestor = GestorUsuarios("usuarios.json")
while True:
    print("\n1.Crear usuario\n2.Listar usuarios\n3.Actualizar usuario\n4.Eliminar usuario\n5.Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Nombre: ")
        email = input("Email: ")
        gestor.crear_usuario(nombre, email)
    elif opcion == "2":
        gestor.listar()
    elif opcion == "3":
        gestor.listar()
        indice = int(input("Seleccione el número del usuario a actualizar: ")) - 1
        nombre = input("Nuevo nombre: ")
        email = input("Nuevo email: ")
        gestor.actualizar(indice, nombre, email)
    elif opcion == "4":
        gestor.listar()
        indice = int(input("Seleccione el número del usuario a eliminar: ")) - 1
        gestor.eliminar(indice)  
    elif opcion == "5":
        print("Saliendo...")
        break