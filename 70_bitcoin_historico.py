import requests
import time
import csv
from datetime import datetime
from pathlib import Path

API_KEY = "bbe7654afcf89c9d24f212bc9696f3efd7d2a3089cc9aa51fa7473c6af521e35"
URL = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

archivo = Path("bitoin_historico.csv")
if not archivo.exists():
    with open(archivo, "w", newline="", encoding="utf-8") as fichero:
        writer = csv.writer(fichero)
        writer.writerow(["Fecha", "Precio USD"])
print("Iniciando la recopilación de datos históricos del Bitcoin...")
try:
    while True:
        try:
            respuesta = requests.get(URL, timeout=10)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                precio = float(datos['data']['priceUsd'])
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(archivo, "a", newline="", encoding="utf-8") as fichero:
                    writer = csv.writer(fichero)
                    writer.writerow([fecha, precio])
                print(f"Datos guardados: {fecha} - ${precio:.2f} USD")
            else:
                print(f"Error al obtener los datos: {respuesta.status_code}")
        except Exception as e:
            print(f"Ocurrió un error al realizar la solicitud: {e}")
        time.sleep(10)
except KeyboardInterrupt:
    print("\nRecopilación de datos detenida por el usuario.")
