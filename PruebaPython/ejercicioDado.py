#Ejercicio para simular un dado
def tirar_dado(caras_dado):
    import random
    return random.randint(1, caras_dado)


#Lo primero vamos a pedir la cantidad de caras del dado
caras_dado = input("¿Cuántas caras tiene el dado? ")

#Ahora vamos a comprobar que la cantidad de caras sea un número entero positivo y mayor que 4
while True:
    if caras_dado.isdigit():
        if  int(caras_dado) < 4 :
            print("El número de caras debe ser mayor o igual que 4.")
        else:   
            break
    else:
        print("La cantidad de caras debe ser un número entero positivo.")

    caras_dado = input("¿Cuántas caras tiene el dado? ")

#Si la cantidad de caras es correcta, vamos a generar un número aleatorio entre 1 y el número de caras del dado
#Para ello, primero vamos a convertir la cadena de entrada a un número entero

caras_dado = int(caras_dado)


#Por último vamos a mostrar el número obtenido

print("El número obtenido es:", tirar_dado(caras_dado))

#Ahora vamos a simular tantos lanzamientos como el usuario quiera y mostrar el resultado de cada lanzamiento en porcentaje

lanzamientos = input("¿Cuántos lanzamientos quieres hacer? ")

while True:
    if lanzamientos.isdigit():
        if int(lanzamientos) > 0 :
            break
        else:
            print("El número de lanzamientos debe ser mayor que 0.")
    else:
        print("La cantidad de lanzamientos debe ser un número entero positivo.")
    lanzamientos = input("¿Cuántos lanzamientos quieres hacer? ")

lanzamientos = int(lanzamientos)

#Tiramos el dado tantas veces como el usuario ha indicado y metemos en una tupla los resultados obtenidos

resultados = tuple(tirar_dado(caras_dado) for i in range(lanzamientos))

#Ahora vamos a mostrar el resultado de cada lanzamiento en porcentaje

for i, resultado in enumerate(resultados, start=1):
    print(f"Lanzamiento {i}: {resultado}")

#Calculamos la frecuencia de cada número y lo convertimos a porcentaje

frecuencias = {i: resultados.count(i) for i in range(1, caras_dado+1)}

for numero, frecuencia in frecuencias.items():
    porcentaje = (frecuencia / lanzamientos) * 100
    print(f"La frecuencia de {numero} es: {porcentaje:.2f}%")

#Y mostramos el número más frecuente

max_frecuencia = max(frecuencias.values())
numero_mas_frecuente = [numero for numero, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]

print(f"El número más frecuente es: {numero_mas_frecuente[0]} con una frecuencia de: {max_frecuencia}, {float((frecuencia / lanzamientos) * 100):.2f}%")