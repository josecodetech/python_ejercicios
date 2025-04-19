tareas = []
#print(type(tareas))
tareas.append("Hacer la compra")
tareas.append("Limpiar la casa")    
tareas.append("Estudiar Python")
tareas.append("Hacer la comida")
tareas.append("Hacer ejercicios de Python")
# consultar la lista de tareas
print("Lista de tareas:")
for tarea in tareas:
    print("-",tarea)
# eliminar una tarea
tareas.remove("Hacer la comida")
print("Lista de tareas después de eliminar una:")
for tarea in tareas:
    print("-",tarea)