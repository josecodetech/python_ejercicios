frutas = ["manzana", "banana", "kiwi", "naranja","manzana"]
print("Lista original:", frutas)
print(type(frutas))
unicas = set(frutas)
print("Lista sin duplicados:", unicas)
print(type(unicas))
for fruta in unicas:
    print(fruta)