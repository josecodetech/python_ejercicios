class Usuario:
    """
    Representa un usuario con nombre y email.
    """
    def __init__(self, nombre, email):
        """
        Inicializa un nuevo usuario.
        Parametros: 
        nombre (str): Nombre del usuario.
        email (str): Email del usuario.
        """
        self.nombre = nombre
        self.email = email
print(Usuario.__doc__)  
jose = Usuario("José", "josecode@gmail.com")
print(jose.__doc__)
help(jose)
print(jose.__init__.__doc__)