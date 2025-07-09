import time

def medir_tiempo(funcion):
    def wrapper():
        inicio = time.time()
        funcion()
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
    return wrapper

@medir_tiempo
def tarea_lenta():
    print("Empieza tarea...")
    time.sleep(2)
    print("Tarea terminada.")

tarea_lenta()