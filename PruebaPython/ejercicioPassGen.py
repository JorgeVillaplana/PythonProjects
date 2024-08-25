#Ejercicio para hacer un generador de contraseñas según ciertos parámetros que elija el usuario

#Primero de todo, importamos la biblioteca random
import random

#Voy a hacer una función que pregunte al usuario la longitud de la contraseña
def longitud_correcta():
    longitud = input("¿Cuántos caracteres desea en la contraseña? ")

    #Comprobamos que la contraseña sea un número entero y positivo
    while True:
        if(longitud.isdigit()):
            if(int(longitud) > 0):
                return int(longitud)
        longitud = input("Por favor, introduce un número entero positivo. ¿Cuántos caracteres desea en la contraseña? ")
    
    return 16

#Ahora preguntamos si quiere incluir letras minúsculas
def incluye_minusculas():
    incluye_minusculas = input("¿Desea incluir letras minúsculas en la contraseña? (S/N) ")

    #Comprobamos que la respuesta sea sí o no

    while True:
        if(incluye_minusculas.upper().strip() == "S"):
            return True
        if(incluye_minusculas.upper().strip() == "N"):
            return False
        incluye_minusculas = input("Por favor, introduce 'S' o 'N'. ¿Desea incluir letras minúsculas en la contraseña? ")

    return True

#Ahora preguntamos si quiere incluir letras mayúsculas

def incluye_mayusculas():
    incluye_mayusculas = input("¿Desea incluir letras mayúsculas en la contraseña? (S/N) ")

    #Comprobamos que la respuesta sea sí o no
    while True:
        if(incluye_mayusculas.upper().strip() == "S"):
            return True
        if(incluye_mayusculas.upper().strip() == "N"):
            return False
        incluye_mayusculas = input("Por favor, introduce 'S' o 'N'. ¿Desea incluir letras mayúsculas en la contraseña? ")

    return True

#Ahora preguntamos si quiere incluir números

def incluye_numeros():
    incluye_numeros = input("¿Desea incluir números en la contraseña? (S/N) ")

    #Comprobamos que la respuesta sea sí o no
    while True:
        if(incluye_numeros.upper().strip() == "S"):
            return True
        if(incluye_numeros.upper().strip() == "N"):
            return False
        incluye_numeros = input("Por favor, introduce 'S' o 'N'. ¿Desea incluir números en la contraseña? ")

    return True

#Ahora preguntamos si quiere incluir símbolos  

def incluye_simbolos():
    incluye_simbolos = input("¿Desea incluir símbolos en la contraseña? (S/N) ")

    #Comprobamos que la respuesta sea sí o no
    while True:
        if(incluye_simbolos.upper().strip() == "S"):
            return True
        if(incluye_simbolos.upper().strip() == "N"):
            return False
        incluye_simbolos = input("Por favor, introduce 'S' o 'N'. ¿Desea incluir símbolos en la contraseña? ")

    return True

#Ahora definimos las letras y números que pueden aparecer en la contraseña
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_mayusculas = letras_minusculas.upper()
numeros = "0123456789"
simbolos = "!@#$%^&*()-_=+[{]};:,.<>/?"

#Ahora solicitamos al usuario los parámetros de la contraseña
lista_parametros = [incluye_minusculas(), incluye_mayusculas(), incluye_numeros(), incluye_simbolos()]
lista_opciones = [letras_minusculas, letras_mayusculas, numeros, simbolos]
lista_caracteres = []

for param, option in zip(lista_parametros, lista_opciones):
    if param:
        lista_caracteres.append(option)

#Generamos la contraseña según los parámetros elegidos
password = ""

longitud = longitud_correcta()
while len(password) < longitud:
    password += random.choice(random.choice(lista_caracteres))

print("Tu contraseña es:", password)