class Conexion:
    def __init__(self):
        print("Conexión establecida")
    def __del__(self):
        print("Conexión cerrada")
conexion1 = Conexion()
conexion2 = Conexion()
del conexion1
del conexion2
