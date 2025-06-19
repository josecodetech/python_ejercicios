class Motor:
    def arrancar(self):
        print("El motor está arrancando.")
class Coche:
    def __init__(self):
        self.motor = Motor() # Composición: Coche tiene un Motor
    def arrancar(self):
        self.motor.arrancar()  # Delegación: Coche delega en Motor
mi_coche = Coche()
mi_coche.arrancar()  # Llamada al método arrancar del coche, que a su vez llama al motor
# Salida esperada: "El motor está arrancando."