
import requests
import time

API_KEY ='pontuapikey' // Reemplaza con tu propia API key
CIUDAD = "Sevilla"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CIUDAD}&appid={API_KEY}&units=metric&lang=es"
def obtener_clima(intentos=3, espera=5):
    for intento in range(1,intentos+1):
        try:
            print(f"Intento {intento}...")
            r = requests.get(URL, timeout=10)
            r.raise_for_status() // Lanza un error si la respuesta no es 200
            datos = r.json()
            temp = datos['main']['temp']
            print(f"La temperatura actual en {CIUDAD} es {temp}°C")
            return  
        except requests.RequestException as e:
            print(f"Error: {e}")
            if intento < intentos:
                print(f"Reintentando en {espera} segundos...")
                time.sleep(espera)
            else:
                print("No se pudo obtener el clima después de varios intentos.")

obtener_clima()
