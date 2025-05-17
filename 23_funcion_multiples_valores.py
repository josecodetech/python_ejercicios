def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta  # Devuelve dos valores

resultado_suma, resultado_resta = operaciones(10, 5)
print("Suma:", resultado_suma)    # Suma: 15
print("Resta:", resultado_resta)  # Resta: 5
resultados = operaciones(20, 10)
print(resultados)
print(type(resultados))  # <class 'tuple'>
print("Suma:", resultados[0])    # Suma: 30
print("Resta:", resultados[1])  # Resta: 10