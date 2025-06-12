class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}€" 
p = Producto("Camiseta", 19.99)
print(p)  # Imprime: Producto: Camiseta, Precio: 19.99€

