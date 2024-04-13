# 1

def my_func(x):
    return x * 11


lst = [12, 24, 36, 48, 109, 187]

print(list(map(my_func, lst)))  # a
print(list(map(lambda x: x * 11, lst)))  # b


# 2
l1 = [8, 9, 2, 6, 1, 2, 3, 1, 2, 1, 3]
l2 = [7, 4, 9, 5, 9, 8, 7, 9, 8, 9, 7]

list3 = list(map(lambda x, y: x * y, l1, l2))
print(list3)

# 3
list4 = list(map(lambda x: x * 4, l1))

even = list(filter(lambda x: (x % 2 == 0), list4)),
odd = list(filter(lambda x: (x % 2 != 0), list4)),

print(f'четные числа {even}')
print(f'нечетные числа {odd}')

