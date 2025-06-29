def registrar_usuario(nombre, email):
    assert "@" in email, "El email no es valido"
    return {
        "nombre": nombre,
        "email": email}
usuario = registrar_usuario("Juan Perez", "juan_gmail.com")
print(f"Usuario registrado: {usuario['nombre']} con email {usuario['email']}")