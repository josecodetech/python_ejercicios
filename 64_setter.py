class Producto:
    def __init__(self, precio):
        self._precio = precio  # Atributo protegido
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >=0:
            self._precio = nuevo_precio
p = Producto(100)
p.precio = 125
print(p.precio)  # Acceso al precio a través del getter

