def parse_phone(ps):
    return ''.join([i.strip() for i in ps.split('-')])


phone_str = str(input('введите номер телефона через "-": '))
print('ваш номер: ', parse_phone(phone_str))

