import requests
url = "https://jsonplaceholder.typicode.com/posts"
nuevo_post = {
    "title":"Nuevo post",
    "body":"Contenido del nuevo post",
    "userId":1
}
respuesta = requests.post(url, json=nuevo_post)
print(f"Estado de la respuesta: {respuesta.status_code}")
print(f"Datos del nuevo post: {respuesta.json()}")