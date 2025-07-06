class UsuarioExistenteError(Exception):
    pass
usuarios_registrados = ["ana@gmail.com","luis@gmail.com"]
def registrar_usuario(email):
    if email in usuarios_registrados:
        raise UsuarioExistenteError(f"El usuario {email} ya está registrado.")
    usuarios_registrados.append(email)
try:
    registrar_usuario("jose@gmail.com")
    print("Usuario registrado correctamente.")
    
except UsuarioExistenteError as e:
    print(f"Error: {e}")
finally:
    print(f"Usuarios registrados: {usuarios_registrados}")
    print("Proceso de registro finalizado.")