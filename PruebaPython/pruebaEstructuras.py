#Estructuras de datos

#Listas: Básicamente son ArrayLists que contienen lo que les de la gana
#Se puede añadir y eliminar elementos a placer.
#https://ellibrodepython.com/listas-en-python

list = [ 'Patata', 4, 'Chanchito', 56, 4.16]

list.append([4,5,'OuhYeah'])
#list.sort() #Esto solo funciona en listas cuyo contenido es todo del mismo tipo.
#Ahora mismo arroja un error porque dice que no puede ordenar int y str juntos.
num_list = [33,56,94, 21, 12, 5452]
num_list.sort() #Si intento usar el sort directamente en el print, me enseña None
#Curiosamente solo por usar el sort ya se guarda la lista directamente en su propio objeto ordenada

print(list)

print(num_list)

for num in num_list :
    print("Value: ", num)