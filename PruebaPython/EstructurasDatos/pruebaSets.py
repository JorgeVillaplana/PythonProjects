#Estructuras de datos

#Set: Son similares a las listas, pero no permiten elementos repetidos
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