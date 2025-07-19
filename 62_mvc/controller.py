from model import Usuario
from view import mostrar_usuario

def main():
    user = Usuario("Ana")
    mostrar_usuario(user)
if __name__ == "__main__":
    main()