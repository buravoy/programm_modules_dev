def parse_full_name(fn):
    fn_arr = fn.split()
    return (f'Ваша фамилия: {fn_arr[0]}\n'
            f'Ваше имя: {fn_arr[1]}\n'
            f'Ваше отчество: {fn_arr[2]}\n')


full_name = str(input('Введите Ваше ФИО: '))
print(parse_full_name(full_name))

