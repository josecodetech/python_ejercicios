class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre # Encapsulamiento del atributo
    def obtener_nombre(self):
        return self.__nombre
usuario = Usuario("Jose")
print(usuario.obtener_nombre())  # Acceso al nombre a través del método