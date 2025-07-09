def mi_decorador(funcion_original):
    def nueva_funcion():
        print("Antes de ejecutar")
        funcion_original()
        print("Después de ejecutar")
    return nueva_funcion
@mi_decorador
def saludar():
    print("Hola!")
saludar()