import argparse

parser = argparse.ArgumentParser(description = "Ejemplo de uso de argparse")
parser.add_argument("--nombre", type=str, help="Nombre del usuario")
parser.add_argument("--edad", type=int,default=18, help="Edad del usuario")
args = parser.parse_args()
print(f"Hola {args.nombre}, tienes {args.edad} años.")