class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    def __repr__(self):
        return f"Ejemplo: Persona(nombre={self.nombre}, edad={self.edad})"
persona = Persona("Juan", 30)
print(persona)
persona2 = Persona("Ana", 25)
print(persona2)
print(repr(persona))