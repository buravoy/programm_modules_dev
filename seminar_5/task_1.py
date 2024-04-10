def square(n):
    return n ** 2


def print_square(n):
    print(f'Квадрат числа равен: {n}')


def print_get_square(n):
    return print_square(square(n))


print_get_square(6)


