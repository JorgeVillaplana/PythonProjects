#Introducción
#En este ejercicio, practicará el flujo de control con bucles para resolver problemas. Se le dará una lista de números enteros y tendrá que añadir algo de código para encontrar un número concreto en una lista y devolverlo. 
#Instrucciones
#1.  En la lista num_list cree un nuevo bucle for e imprima cada valor de la lista en orden secuencial.
#2.  Dentro del bucle for, cree una condición que busque todos los números que sean mayores que 45 e imprima sólo los números que cumplan esa condición
#3.  Cambie la sentencia print por "Mayor de 45" y añada una condición else con una sentencia print de "Menor de 45".
#4.  Actualice el bucle for para utilizar la función enumerar de forma que pueda obtener y utilizar el índice. Modifique la condición para que busque el número 36 e imprima lo siguiente 'Número encontrado en la posición: ', número índice
#5.  A continuación, cree una nueva variable llamada count, asígnele el valor 0 y colóquela fuera del bucle for.
#6.  Dentro del bucle for incremente el contador en 1.
#7.  Añada una sentencia print fuera del bucle for para imprimir el valor de la variable count.
#8.  Por último, añada una sentencia break directamente después de la sentencia print dentro de la condición if para encontrar el número.
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

#1.   En la lista num_list cree un nuevo bucle for e imprima cada valor de la lista en orden secuencial.
print("Ejercicio nº 1")
for num in num_list :
    print (num)
    
#2.  Dentro del bucle for, cree una condición que busque todos los números que sean mayores que 45 e imprima sólo los números que cumplan esa condición
print("Ejercicio nº 2")
for num in num_list :
    if num > 45 :
        print (num)

#3.  Cambie la sentencia print por "Mayor de 45" y añada una condición else con una sentencia print de "Menor de 45".
print("Ejercicio nº 3")
for num in num_list :
    if num < 45 :
        print (num)
        
#4.  Actualice el bucle for para utilizar la función enumerar de forma que pueda obtener y utilizar el índice. Modifique la condición para que busque el número 36 e imprima lo siguiente 'Número encontrado en la posición: ', número índice
print("Ejercicio nº 4")
for pos , num in enumerate(num_list) :
    if num == 36 :
        print("Número " + str(num) + " encontrado en la posición: " + str(pos))
        
#5.  A continuación, cree una nueva variable llamada count, asígnele el valor 0 y colóquela fuera del bucle for.
#6.  Dentro del bucle for incremente el contador en 1.
#7.  Añada una sentencia print fuera del bucle for para imprimir el valor de la variable count.
print("Ejercicio del 5 al 7")
count = 0
for pos , num in enumerate(num_list) :
    if num == 36 :
        print("Número " + str(num) + " encontrado en la posición: " + str(pos))
    count += 1
print("Count: "+str(count))

#8.  Por último, añada una sentencia break directamente después de la sentencia print dentro de la condición if para encontrar el número.
print("Ejercicio nº 8")
count = 0
for pos , num in enumerate(num_list) :
    if num == 36 :
        print("Número " + str(num) + " encontrado en la posición: " + str(pos))
        break
    count += 1
print("Count: " + str(count))