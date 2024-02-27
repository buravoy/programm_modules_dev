string = input('Ввести существительное: ')


f_letter = string[0]

if f_letter.upper() == f_letter:
    print('Это имя собственное')
else:
    print('Это имя нарицательное')

