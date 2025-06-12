# Creamos la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
# Creamos una instancia de la clase Persona
persona1 = Persona("Juan", 30)
persona1.saludar()
# Creamos otra instancia de la clase Persona
persona2 = Persona("Ana", 25)
persona2.saludar()
persona1.nombre = "Carlos"
persona1.saludar()