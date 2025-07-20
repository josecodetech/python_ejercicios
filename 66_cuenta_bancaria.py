class CuentaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self._saldo = saldo
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
        else:
            print("Ingreso no válido")
    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
        else:
            print("Retiro no válido")
    def __str__(self):
        return f"Cuenta de {self.titular} con saldo: {self._saldo}"
cuenta = CuentaBancaria("Maria", 1000)
cuenta.ingresar(500)
print(cuenta)  # Imprime: Cuenta de Maria con saldo: 1500
cuenta.retirar(200)
print(cuenta)  # Imprime: Cuenta de Maria con saldo: 1300
