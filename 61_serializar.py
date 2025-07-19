import pickle

datos = {
    'nombre': 'Juan',
    'edad': 30,}
with open('datos.pkl', 'wb') as fichero:
    pickle.dump(datos, fichero)

print("Datos serializados y guardados en 'datos.pkl'.")

with open('datos.pkl', 'rb') as fichero:
    datos_cargados = pickle.load(fichero)
print(f"Datos cargados: {datos_cargados}")