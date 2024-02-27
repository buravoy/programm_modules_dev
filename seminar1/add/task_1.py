def get_sun_time(day_number):
    return ((day_number - 1) * 3) + 1


day = int(input('введите номер дня '))
print('можно греться', get_sun_time(day), 'минут')

