import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
respuesta = requests.get(url)
if respuesta.status_code == 200:
    datos = respuesta.json()
    print(f"Titulo: {datos['title']}")
else:
    print(f"Error al obtener los datos: {respuesta.status_code}")
