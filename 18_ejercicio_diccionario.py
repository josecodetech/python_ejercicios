contacto = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "email": "jdkjf@gmail.com"}
print("Datos del contacto: ")
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")

# modificar la edad
contacto["edad"] = 54
# eliminar el email
del contacto["email"]
print("Datos del contacto después de modificar la edad y eliminar el email: ")
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")