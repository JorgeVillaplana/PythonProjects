#Función que crea un fichero vacío con el nombre dado
#en caso de que no exista.
def crea_fichero(nombre):
    try:
        with open(nombre, 'x', 'utf-8') as file:
            pass
        return True
    except FileExistsError:
        return False

control = True
while control:
    try:
        nombre_archivo = 'nuevo_archivo.txt'
        with open(nombre_archivo, 'r+') as file:
            file.writelines('Hola, esto es una prueba.\n\n') #Esto escribe la primera línea del archivo siempre
            
        with open(nombre_archivo, 'a') as file:
            lines = ['Cuackabilly MacPato estuvo aquí', 'El Barto', 'Megakabuterimon', 'Emosido engañado']
            file.writelines( map( lambda x: x + '\n', lines) )
            
        break
    except FileNotFoundError:
        control = crea_fichero(nombre_archivo)