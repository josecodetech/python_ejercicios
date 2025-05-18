entrada = input("Introduce un número: ")
try:
    numero = float(entrada)
    print(f"El número introducido es: {numero}")
except ValueError:
    print("Error: No se ha introducido un número válido.")
    