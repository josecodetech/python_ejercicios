def dividir(a,b):
    assert b != 0, "No se puede dividir por cero"
    return a / b
#print(dividir(10, 2))  # Esto debería funcionar
#print(dividir(10, 0))  # Esto debería lanzar una excepción AssertionError
try:
    resultado = dividir(10, 0)
    print(f"Resultado de la división: {resultado}")
except AssertionError as e:
    print(f"Error capturado: {e}")