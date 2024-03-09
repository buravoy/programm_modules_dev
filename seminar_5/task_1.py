def square(n):
    return n ** 2


def print_square(n):
    print(f'Квадрат числа равен: {n}')


def print_get_square(n):
    sq = square(n)
    print_square(sq)
    return sq


print_get_square(2)


