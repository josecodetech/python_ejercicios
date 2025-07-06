class EdadInvalidaError(Exception):
    pass
def verificar_edad(edad):
    if edad < 18:
        raise EdadInvalidaError("Debes ser mayor de edad.")
verificar_edad(15)
