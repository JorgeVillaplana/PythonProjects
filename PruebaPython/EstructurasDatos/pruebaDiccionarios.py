#Estructuras de Datos

#Diccionarios: Son como las lista, pero cada elemento tiene clave : valor
#Lo bueno que tienen es que puedes acceder al elemento por su clave
#Se parecen bastante a los archivos JSON
#Cada clave debe ser única, si no sólo accede al último elemento con esa clave
prueba_diccionario = { 'Palabra' : 'Texto' , 1 : 'Cuack', (3, 'Patata') : 9, 1 : { 0 : 36, 5 : 'Zubizarreta'}}
print(f'Diccionario completo: {prueba_diccionario}')
print(f'Accediendo al primer elemento por la clave: {prueba_diccionario['Palabra']}')
#print(f'Accediendo al primer elemento por la posición: {dict_test[0]}')  #No funciona, hay que acceder siempre por clave
print(f'Accediendo al diccionario anidado: {prueba_diccionario[1]}')
print(f'Accediendo a un elemento del diccionario anidado: {prueba_diccionario[1][5]}')

#Pruebas de iteración
print('Prueba de iteración 01: Imprimiendo las claves del diccionario')
for x in prueba_diccionario :
    print(x) #Imprime las claves del diccionario, se salta los duplicados

print('Prueba de iteración 02: Imprimiendo los valores del diccionario')
for x in prueba_diccionario:
    print(prueba_diccionario[x]) #Curiosamente, cuando ha llegado a la primera clave 1 imprime el valor del último 1
    
print('Prueba de iteración 03: Imprimir clave y valor al mismo tiempo')
for x, y in prueba_diccionario.items():
    print(f'Clave: {x} ; Valor: {y}')