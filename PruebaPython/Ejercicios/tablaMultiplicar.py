#Dado un número n, mostrar su tabla de multiplicar
n = int(input('Introduce un número: '))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")