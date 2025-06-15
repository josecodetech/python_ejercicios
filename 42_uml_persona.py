class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
Jose = Persona("José", 30)
Maria = Persona("María", 25)
print(Jose.saludar())  # Imprime: Hola, me llamo José y tengo 30 años.
print(Maria.saludar())  # Imprime: Hola, me llamo María y tengo 25 años.