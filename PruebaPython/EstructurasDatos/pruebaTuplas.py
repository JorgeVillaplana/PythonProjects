#Estructuras de datos

#Tuplas: Son como las listas pero no se puede modificar su contenido
#Es decir, no se puede cambiar ninguno de sus elementos ni se puede
#añadir o borrar elementos de la tupla
#Básicamente como si fuera una lista pero constante
tuple = 4, 9, 3.65, 'Ouh yeah', (1, 2, 3)
print("Muestro el tipo de la tupla para confirmar que lo es:")
print(type(tuple)) #Muy útil el método type() para saber de qué tipo es una variable o cualquier cosa
print("Mostramos la tupla:")
print(tuple)
for element in tuple:
    print(type(element))

#Métodos de las tuplas
#count() Cuenta la cantidad de veces que se repite un elemento concreto
print('Método count():')
print(tuple.count(9))

#index() Pasa la posición del argumento al que le pasamos. En caso de no enontrarlo lanza una excepción
#ValueError: tuple.index(x): x not in tuple
print('Método index() al que vamos a buscar el número 3.65')
print(tuple.index(3.65))