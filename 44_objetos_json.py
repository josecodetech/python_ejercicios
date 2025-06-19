import json
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    def to_dict(self):
        return {"nombre": self.nombre, "email": self.email}
usuarios = [Usuario("Ana", "ana@gmail.com"), Usuario("Luis", "luis@gmail.com")]
with open("usuarios.json", "w", encoding="utf-8") as f:
    json.dump([u.to_dict() for u in usuarios], f, indent=4)
    print("Datos guardados en usuarios.json")
with open("usuarios.json", "r", encoding="utf-8") as f:
    datos = json.load(f)
    print("Datos cargados desde usuarios.json")

usuarios_cargados = [Usuario(**d) for d in datos]
for u in usuarios_cargados:
    print(f"{u.nombre} - {u.email}")

