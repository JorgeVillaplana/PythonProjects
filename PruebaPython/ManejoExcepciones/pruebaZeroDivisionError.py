def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'No se puede dividir por 0'


ans = divide_by(40, 0)
print(ans)
