try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('Archivo no encontrado.')