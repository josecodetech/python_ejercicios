class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
    def __eq__(self, otro):
        return self.titulo == otro.titulo
libro1 = Libro("1984")
libro2 = Libro("1984")
print(libro1 == libro2)  # Imprime: True
libro3 = Libro("Brave New World")   
print(libro1 == libro3)  # Imprime: False