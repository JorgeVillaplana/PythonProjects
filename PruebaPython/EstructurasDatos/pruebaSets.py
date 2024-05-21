#Estructuras de datos

#Set: Son similares a las tuplas (son inmutables), pero no permiten elementos repetidos
#Además, tampoco permiten listas o diccionarios como parte de sus elementos
#Por lo demás parecen potentes, las interacciones entre sets me recuerdan a las
#consultas SQL, ya que permiten unión, o ver las diferencias.

#Para probar los sets voy a declarar 3 sets diferentes con números enteros y
#elementos comunes entre sí
set_a = {1, 2, 3, 4, 5, 6}
set_b = {4, 5, 6, 7, 8, 9}
set_c = {1, 2, 3, 7, 8, 9}

#Lo primero va a ser imprimir los 3 y ver cómo se itera al menos uno
print(set_a)
print(set_b)
print(set_c)

print('Iteramos con enumerate')
for pos, num in enumerate(set_a) :
    print(f'Posición: {pos} -> Valor: {num}')
    
#Ahora vamos a probar a unir los sets mientras los iteramos
print('Volvemos a iterar mientras unimos')
for pos, num in enumerate(set_a | set_b | set_c) :
    print(f'Posición: {pos} -> Valor: {num}')
    
# Vamos a probar la función len para ver el tamaño de un set
print(f'El tamaño de set_a es {len(set_a)}')

# Ahora vamos a ver una comprobación de que un set tiene un elemento
print(f'El set a tiene el num 3 : {3 in set_a}')

# Ahora voy a añadir un elemento a un set
set_c.add(11)
print('Hemos añadido un elemento al set_c')
print(f'{set_c}')

# Para borrar un elemento existen dos métodos, remove y discard.
# Remove busca el elemento y lo borra, pero si no lo encuentra lanza una excepción.
# Discard hace lo mismo, pero en caso de no encontrar el elemento no hace nada, simplemente continúa la ejecución del programa
print('Probando los métodos remove y discard')
print('Primero añado una tupla')
set_c.add((17, 19))
print(set_c)
print('Ahora voy a borrar el 11 con un remove')
set_c.remove(11)
# print('Y voy a probar remove con un 14')
# set_c.remove(14)
# Probado, efectivamente arroja un error y me interrumpe la ejecución
print('Ahora voy a borrar la tupla (17, 19) con discard')
set_c.discard((17,19))
print(set_c)
print('Y ahora vamos a usar discard para borrar un str Patata')
set_c.discard('Patata')
print(set_c)
# También existe la función pop para borrar un elemento aleatorio del set
# No termino de entender para qué hace falta tener un método específico para
# borrar un elemento aleatorio, pero bueno, vamos a probarlo con otro set nuevo
# a ver qué pasa
print('Creamos un set nuevo para probar pop()')
set_frutas = {'Naranja', 'Sandía', 'Kiwi', 'Pera', 'Manzana'}
print(set_frutas) #Estoy viendo que cada vez que ejecuto el programa ordena el set de una forma diferente ¿en base a qué?
set_frutas.add('Granada')
print(set_frutas) #Por lo visto cada vez que añado un elemento puede reordenarse otra vez el set
set_frutas.add('Mango')
print(set_frutas)
print('Ahora vamos a probar el pop y ver qué elemento se carga')
set_frutas.pop()
print(set_frutas) #Efectivamente, tras ejecutar el programa varias veces podemos ver que el pop se carga un elemento al completo azar
del set_frutas



#Ver más métodos como:
# s1.union(s2[, s3 ...])
# s1.intersection(s2[, s3 ...])
# s1.difference(s2[, s3 ...])
# s1.symmetric_difference(s2)
# s1.isdisjoint(s2)
# s1.issubset(s2)
# s1.issuperset(s2)
# s1.update(s2[, s3 ...])
# s1.intersection_update(s2[, s3 ...])
# s1.difference_update(s2[, s3 ...])
# s1.symmetric_difference_update(s2)
