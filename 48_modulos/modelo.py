class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    def to_dict(self):
        return {"nombre": self.nombre, "email": self.email}
    