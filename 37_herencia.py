class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        return f"{self.nombre} hace un sonido."
class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} guau!.")
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} miau!.")
perro = Perro("Rex")
gato = Gato("Michi")
perro.hablar()
gato.hablar()