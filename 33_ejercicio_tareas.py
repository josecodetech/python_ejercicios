
import os
import json

archivo = "tareas.json"
# cargar tareas desde un fichero
def cargar_tareas():
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"pendientes": [], "completadas": []}
# guardar tareas en un fichero
def guardar_tareas(tareas):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4)
# mostrar tareas
def mostrar_tareas(lista, titulo):
    print(f"\n {titulo}:")
    if lista:
        for i, tarea in enumerate(lista, start=1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas en esta lista.")
# menu principal
def menu():
    tareas = cargar_tareas()
    while True:
        print("\n--- MENU ---")
        print("1. Añadir tarea")
        print("2. Ver pendientes")
        print("3. Marcar como completada")
        print("4. Ver completadas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nueva = input("Ingrese la nueva tarea: ")
            tareas["pendientes"].append(nueva)
            guardar_tareas(tareas)
        elif opcion == "2":
            mostrar_tareas(tareas["pendientes"], "Tareas Pendientes")
        elif opcion == "3":
            mostrar_tareas(tareas["pendientes"], "Tareas Pendientes")
            if tareas["pendientes"]:
                try:
                    num = int(input("Numero de tarea completada: ")) - 1
                    completada = tareas["pendientes"].pop(num)
                    tareas["completadas"].append(completada)
                    guardar_tareas(tareas)
                except (ValueError, IndexError):
                    print("Número inválido. Intente de nuevo.")
        elif opcion == "4":
            mostrar_tareas(tareas["completadas"], "Tareas Completadas")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
# ejecutar el menu
menu()