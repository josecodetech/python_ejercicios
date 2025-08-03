import requests

API_KEY = "bbe7654afcf89c9d24f212bc9696f3efd7d2a3089cc9aa51fa7473c6af521e35"
URL = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
try:
    respuesta = requests.get(URL)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        precio = float(datos['data']['priceUsd'])
        print(f"El precio actual del Bitcoin es: ${precio:.2f} USD")
    else:
        print(f"Error al obtener los datos: {respuesta.status_code}")
except Exception as e:
    print(f"Ocurrió un error al realizar la solicitud: {e}")

