from gestor import GestorUsuarios
from utilidades.helpers import limpiar_texto

gestor = GestorUsuarios("usuarios.json")
# aqui menu de opciones
while True:
    print("\n1.Crear usuario\n2.Listar usuarios\n3.Actualizar usuario\n4.Eliminar usuario\n5.Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Nombre: ")
        nombre = limpiar_texto(nombre)
        email = input("Email: ")
        email = limpiar_texto(email)
        gestor.crear_usuario(nombre, email)
    elif opcion == "2":
        gestor.listar()
    elif opcion == "3":
        gestor.listar()
        indice = int(input("Seleccione el número del usuario a actualizar: ")) - 1
        nombre = input("Nuevo nombre: ")
        email = input("Nuevo email: ")
        gestor.actualizar(indice, nombre, email)
    elif opcion == "4":
        gestor.listar()
        indice = int(input("Seleccione el número del usuario a eliminar: ")) - 1
        gestor.eliminar(indice)  
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
