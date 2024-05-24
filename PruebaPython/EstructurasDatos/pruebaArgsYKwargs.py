#Estructuras de datos | Parámetros de entrada en las funciones

# Los *args son una forma de expresar que una función puede expresar que la
# función va a recibir una cantidad intdeterminada de argumentos.
# Los **kwargs son como los args pero espera que cada uno de los parámetros sean
# clave=valor. 

# Para probarlo, voy a definir 3 funciones, uno con 3 parámetros, otra con *args y
# otra con **kwargs
# Función suma con 3 parámetros
def suma_params (a, b, c):
    return a + b + c

# Función suma con un número de argumentos indeterminado
def suma_args (*args):#Realmente no hace falta llamar al parámetro args, lo importante es el *
    suma = 0
    
    for arg in args:
        suma += arg
    
    return suma

# Función suma a la que se le pasa un número de argumentos indeterminado, siendo
# cada argumento un par de clave - valor
def suma_kwargs (**kwargs):#Realmente no hace falta llamar al parámetro kwargs, lo importante es el **
    suma = 0
    
    for key, value in kwargs.items():
        print(f'Clave = {key} , Valor = {value}')
        suma += value
    
    return suma

# También podemos mezclarlo todo como queramos
def suma_todo (a, b, *args, **kwargs):
    suma = a + b
    s_args = 0
    s_kwargs = 0
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')
    for arg in args:
        if isinstance(arg, int):
            s_args += arg
    
    for key, value in kwargs:
        s_kwargs += value
    
    print(f'Suma: {suma}, S_args: {s_args}, S_kwargs: {s_kwargs}')
    return suma + s_args + s_kwargs

# Ahora vamos a invocar y probar esas funciones, mostrando el resultado de cada una
alto = 80
ancho = 30
hondo = 45

# Primero la suma con los parámetros
print(suma_params(alto, ancho, hondo))

# Ahora la suma con *args
print(suma_args(alto, ancho, hondo))

# Y ahora la suma con los kwargs, aprovechando para cambiarle el valor a las variables
#print(suma_kwargs(alto=10, ancho=20, hondo=15)) #Da error, no puedo usar variables ya definidas para usar los kwargs
print(suma_kwargs(nuevo_alto=10, nuevo_ancho=20, nuevo_hondo=15))

# Por último vamos a probar una fución que tenga de todo
arg = [ancho, alto, hondo, 75]
kwarg = {'largo' : 13, 'kiwi' : 78, 'nim' : 1}
print('Probando suma_todo')
print(suma_todo( 22, 45, arg,  kwarg)) #El orden es importante, 
# si después de poner los pares de clave=valor intento meter un valor tal cual, da error
