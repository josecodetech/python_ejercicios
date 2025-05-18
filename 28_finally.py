try:
    print("Ejecutando bloque try")
    resultado = 10 / 2
except Exception as e:
    print("Se ha producido un error:", e)
finally:
    print("Este bloque se ejecuta siempre, haya o no habido una excepción.")
    print("Fin del bloque finally")