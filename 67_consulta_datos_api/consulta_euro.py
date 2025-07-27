import time
import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"
while True:
    try:
        respuesta = requests.get(url)
        if respuesta.ok:
            euro = respuesta.json()["rates"]["EUR"]
            print(f"1 USD = {euro} EUR")
        
    except requests.RequestException.HTTPError as e:
        print(f"Error HTTP: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    time.sleep(5)
    