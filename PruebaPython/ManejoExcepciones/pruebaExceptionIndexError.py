try:
    items = [1,2,3,4,5]
    item = items[6]
    print(item)
except IndexError:
    print('El elemento no existe en la lista')