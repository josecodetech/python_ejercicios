class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
    def get_saldo(self):
        return self.__saldo
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad # equivalente a self.__saldo = self.__saldo + cantidad

    def mostrar_info(self):
        print(f"Titular: {self.__titular}, Saldo: {self.__saldo}")
cuenta = CuentaBancaria("Juan", 1000)
cuenta.mostrar_info()
cuenta.__saldo = 500  # Esto no afectará al saldo real
cuenta.mostrar_info()  # El saldo seguirá siendo 1000
cuenta.depositar(500)
cuenta.mostrar_info()  # Ahora el saldo será 1500