vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in vals:
    print(i)
    if i < 3:
        print('Плохо')
    elif i < 6:
        print('Удовлетворительно')
    elif i < 9:
        print('Хорошо')
    else:
        print('Отлично')
