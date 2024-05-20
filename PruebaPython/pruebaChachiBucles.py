#Archivo para probar las estructuras de los bucles

#Probando bucles con números enteros
#Probando bucle while
a = 2
while a < 99:
    print (str(a) + " elefantes se balanceaban sobre la tela de un while.")
    print("Como veían que no se caían, fueron a llamar a otro elefante.")
    print()
    a += 1 #Importante poner el incremento en el while
    if a >= 33 :
        break #Con esta estructura de control hago que el bucle pare al llegar al 33
del a

#Probando bucle for
for i in range(2,34) : #IMPORTANTE que range(x,n) incluye x pero NO n
    if i%2 == 0 :
        continue #Con esta estructura de control hago que el bucle se salte los pares
    print (str(i) + " elefantes se balanceaban sobre la tela de un for.")
    print("Como veían que no se caían, fueron a llamar a otro elefante.")
    print()
del i

for i in range(10) : #De esta forma va de 0 a 9
    print (i)
