def saludar(nombre):
    """
    Devuelve un saludo personalizado.

    Parametros:
    nombre (str): El nombre de la persona a saludar.

    Retorna:
    str: Un saludo con el nombre proporcionado.
    """ 
    return f"Hola, {nombre}!"
print(saludar.__doc__)
help(saludar)