def analizar_lista(lista):
    lista_unica = sorted(set(lista))
    conteos = {}
    for num in lista:
        if num in conteos:
            conteos[num] += 1 # conteos[num] = conteos[num] + 1
        else:
            conteos[num] = 1
    numero_mas_frecuente = max(conteos, key=conteos.get)
    repeticiones = conteos[numero_mas_frecuente]
    return lista_unica, numero_mas_frecuente, repeticiones

# Ejemplo de uso
if __name__ == "__main__":
    entrada = [4,2,6,2,2,2,2,8,7,6,9,8,3,4,2,1,5,3,6,8,9,7,4]
    unica, num_frecuente, veces = analizar_lista(entrada)
    print(f"Lista única ordenada: {unica}")
    print(f"Número más frecuente: {num_frecuente} (Repeticiones: {veces})")
    