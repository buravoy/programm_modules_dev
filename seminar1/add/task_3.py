def crete_course(n1, n2, n3):
    return (f'Рецепт\n'
            f'{n1}: 200г.\n'
            f'{n2}: 300г.\n'
            f'{n3}: 100г.\n'
            f'Приправить политической историей. Добавить математические модели по вкусу.')


name1 = str(input('Введите название первого курса: '))
name2 = str(input('Введите название второго курса: '))
name3 = str(input('Введите название третьего курса: '))

print(crete_course(name1, name2, name3))

