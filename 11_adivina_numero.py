import random
# Genera un número aleatorio entre 1 y 100 ambos incluidos
numero_aleatorio = random.randint(1,100)
# Inicializa el número de intentos
intentos = 0
# Inicializa el número ingresado por el usuario
numero_ingresado = 0
# Bucle hasta que el usuario adivine el número
while numero_ingresado != numero_aleatorio:
    # Solicita un número al usuario
    numero_ingresado = int(input("Adivina el número entre 1 y 100: "))
    # Incrementa el contador de intentos
    intentos += 1
    # Compara el número ingresado con el número aleatorio
    if numero_ingresado < numero_aleatorio:
        print("El número es mayor.")
    elif numero_ingresado > numero_aleatorio:
        print("El número es menor.")
# Muestra el número de intentos realizados  
print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
