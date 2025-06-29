while True:
    edad = input("Ingrese su edad: ")
    try:
        edad = int(edad)
        assert edad > 0, "La edad debe ser un número positivo"
        print(f"Edad ingresada correctamente: {edad}")
        break
    except (ValueError, AssertionError) as e:
        print(f"Error: {e}. Intente de nuevo.")
print("Proceso finalizado.") 