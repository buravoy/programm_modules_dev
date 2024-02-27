def parse_int(ns):
    st_arr = ns.split(';')
    return [int(i.strip()) for i in st_arr]


def parse_float(ns):
    st_arr = ns.split(';')
    return [float(i.strip()) for i in st_arr]


num_str = str(input('введите несколько чисел через ";": '))
print('целые: ', parse_int(num_str))
print('дробные: ', parse_float(num_str))
