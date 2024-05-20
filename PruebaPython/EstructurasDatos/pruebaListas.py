#Estructuras de datos

#Listas: Básicamente son ArrayLists que contienen lo que les de la gana
#Se puede añadir y eliminar elementos a placer.
#https://ellibrodepython.com/listas-en-python

#Voy a dejar definida una función para imprimir por pantalla los elementos de
#una lista con posición y valor.
def showList (list) :
    for pos, val in enumerate(list) :
        print("Pos: ", pos, "Num: ", val)

list = [ 'Patata', 4, 'Chanchito', 56, 4.16]

list.append([4,5,'OuhYeah'])#Me anida la lista en vez de añadir 3 elementos
#list.sort() #Esto solo funciona en listas cuyo contenido es todo del mismo tipo.
#Ahora mismo arroja un error porque dice que no puede ordenar int y str juntos.
num_list = [33,56,94, 21, 12, 5452, 596]
num_list.sort() #Si intento usar el sort directamente en el print, me enseña None
#Curiosamente solo por usar el sort ya se guarda la lista directamente en su propio objeto ordenada

print(list)

print(num_list)
#Prueba de iteración de dos listas al mismo tiempo
print("Muestra de iteración de las dos listas a la vez")
for element, num in zip(list, num_list) :
    print("List: ", element, "Num: ", num) #Al tener list un elemento menos, cuando termina
#de iterar el list para y no llega a mostrar el último elemento de num_list
#Vamos a probar ahora a ver qué pasa si le meto dos elementos más a list
list.extend([12.23, "sistemas", 2]) #Con este método, en lugar de anidar la lista, la extiende
print("Segunda prueba, ahora la primera lista es más larga que la segunda")
for element, num in zip(list, num_list) :
    print("List: ", element, "Num: ", num) #En este caso, al terminar de iterar la segunda lista
#para, aunque no haya terminado de iterar la primera
#Conclusión, al iterar dos listas al mismo tiempo con este método 'zip()', la iteración termina
#al terminar cualquiera de las dos listas, con lo que hay que ir con ojo ya que se puede perder
#información

#Probando a eliminar elemento de una lista:
# - Por su posición:
print("Viendo la lista antes de ver si se ha eliminado la posición 3:")
showList(num_list)
del num_list[3]
print("Después de eliminar la posición 3:")
showList(num_list) #Aquí vemos como se ha eliminado la posición 3 pero la lista no deja la posición vacía,
#si no que mueve el resto

#Probando otros métodos de listas:
#Método index
print("Probando método index() pasándole como parámetro Chanchito entre comillas simples")
print(list.index('Chanchito'))

#Método pop() para eliminar
print("Primero vemos la lista completa:")
print(list)
print("Ahora vemos la lista sin el último elemento")
list.pop()
print(list)
print("Ahora vamos a usar pop pero quitando el elemento nº 4")
list.pop(4)
print(list)

#Con esto doy por finalizado las pruebas de las listas