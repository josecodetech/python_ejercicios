class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False
    def devolver(self):
        self.disponible = True
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.prestamos = []
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
    def prestar_libro(self, titulo, email):
        libro = next((l for l in self.libros if l.titulo == titulo and l.disponible), None)
        usuario = next((u for u in self.usuarios if u.email == email), None)
        if libro and usuario:
            if libro.prestar():
                usuario.prestamos.append(libro)
                print(f"{usuario.nombre} ha tomado prestado '{libro.titulo}'.")
            else:
                print(f"El libro '{libro.titulo}' no está disponible.")
miBiblioteca = Biblioteca()
miBiblioteca.registrar_usuario(Usuario("Ana", "prueba@gmail.com"))
miBiblioteca.agregar_libro(Libro("1984", "George Orwell"))
miBiblioteca.agregar_libro(Libro("El Principito", "Antoine de Saint-Exupéry"))
miBiblioteca.prestar_libro("1984", "prueba@gmail.com")