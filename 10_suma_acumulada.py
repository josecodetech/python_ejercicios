cantidad = int(input("Ingrese la cantidad de números a sumar: "))
suma = 0
for i in range(1, cantidad + 1):
    numero = int(input(f"Ingrese el número {i}: "))
    suma += numero # suma = suma + numero
print(f"La suma de los {cantidad} números es: {suma}")