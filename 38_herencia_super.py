class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    def mostrar_info(self):
        print(f"Coche: {self.marca} / {self.modelo}, Puertas: {self.puertas}")
coche1= Coche("Toyota", "Corolla", 4)
coche1.mostrar_info()