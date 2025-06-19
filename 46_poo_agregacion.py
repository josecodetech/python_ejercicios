class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
class Curso:
    def __init__(self, profesor):
        self.profesor = profesor # Agregación: Curso tiene un Profesor
    def mostrar(self):
        print(f"El profesor del curso es {self.profesor.nombre}.")
profe = Profesor("Ana")
curso = Curso(profe)  # Agregación: Curso tiene un Profesor
curso.mostrar()  # Llamada al método mostrar del curso