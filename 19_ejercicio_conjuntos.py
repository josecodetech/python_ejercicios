nombres = {"Juan", "Pedro", "Maria", "Ana", "Luis"}
nombres.add("Carlos")
if "Luis" in nombres:
    print("Luis está en el conjunto de nombres")
nombres.remove("Ana")
print("Conjunto de nombres después de eliminar a Ana:")
for nombre in nombres:
    print("-", nombre)
nombres.add("Carlos")
nombres.add("Carlos")
nombres = {"Juan", "Pedro", "Antonia","Fernando","Lucia","Eva"}
for nombre in nombres:
    print("-", nombre)