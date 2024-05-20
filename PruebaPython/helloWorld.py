#Defino una función para que sume dos números. Tendría que comprobar el tipo de los parámetros para que lo haga bien
#Nota: He visto que si defino la función abajo del programa no me la coge
def suma (a, b):
    return a + b

#Aquí empezaría de verdad el programa
#Declaración de variables
x = 1 + 2\
+ 3.0 #Poner la barrita \ sirve para que python tome la siguiente línea como parte de la primera
bo = True

#Probando estructuras de control
if bo :  #Tengo que probar los operadores ternarios
    print("Probando boolean. Estamos dentro del if true.")
    bo = not bo #He probado a poner directamente 'not bo' y no me ha funcionado, no se si habrá otra manera de hacer lo mismo
if not bo :
    print("Probando boolean. Estamos dentro del if false")
if x < 3 :
    print("La variable del if es " + str(x) + " y es menor a 3")
elif x == 3 :
    print("La variable del if es " + str(x) + " y es igual que 3")
else :
    print("La variable del if es " + str(x) + " y es mayor que 3")
    
print ("Han terminado los if")
del x, bo #Esto sirve para borrar una variable y que deje de ocupar espacio en memoria
#print (suma(int(input("Introduce el primer número: ")) , int(input("Introduce el segundo número: "))))