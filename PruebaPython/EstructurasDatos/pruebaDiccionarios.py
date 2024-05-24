#Estructuras de Datos

#Diccionarios: Son como las lista, pero cada elemento tiene clave : valor
#Lo bueno que tienen es que puedes acceder al elemento por su clave
#Se parecen bastante a los archivos JSON
#Cada clave debe ser única, si no sólo accede al último elemento con esa clave
prueba_diccionario = { 'Palabra' : 'Texto' , 1 : 'Cuack', (3, 'Patata') : 9, 1 : { 0 : 36, 5 : 'Zubizarreta'}}
prueba_diccionario2 = { (3, 'Patata') : 'Actualizado', 'Palabra' : 'Chapata', 8 : 8, 'Verdura' : 'Lombarda' }
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
def print_dictionary (prueba_diccionario): 
    print('Imprimiendo diccionario')
    for x, y in prueba_diccionario.items():
        print(f'Clave: {x} -> Valor: {y}')

#Para imprimir las claves del diccionario:
print(prueba_diccionario.keys())

#Para imprimir el diccionario completo
print(prueba_diccionario.items()) #Curioso que muestre los pares separados por una coma y que los una con paréntesis

#Métodos para trabajar con diccionarios
# Actualizar un diccionario con otro
prueba_diccionario.update(prueba_diccionario2)
print_dictionary(prueba_diccionario)

# Borrar un elemento (clave:valor) de un diccionario usando la clave como parámetro
print(prueba_diccionario.pop((3, 'Patata'))) # La función pop(clave) devuelve el valor del item borrado
print_dictionary(prueba_diccionario)

# Borrar un item aleatorio de un diccionario
print(prueba_diccionario2.popitem()) #popitem() devuelve el par clave,valor
print_dictionary(prueba_diccionario2) #Se supone que se carga un valor aleatorio, pero parece que tiene tendencia a borrar el último

# Borrar todo el diccionario
prueba_diccionario2.clear()
print_dictionary(prueba_diccionario2) #No termino de entender para qué querría esto