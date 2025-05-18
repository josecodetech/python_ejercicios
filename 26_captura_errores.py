try:
    num1 = float(input("Introduce el numerador: "))
    num2 = float(input("Introduce el denominador: "))
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")