import os

carpeta = "D:\\Workspace\\WorkspaceTutorialEjerciciosPython\\66_automatizacion_tareas\\logs"
for archivo in os.listdir(carpeta):
    if archivo.endswith(".log"):
        os.remove(os.path.join(carpeta, archivo))
        print(f"Archivo eliminado: {archivo}")
    else:
        print(f"Archivo no eliminado (no es .log): {archivo}")