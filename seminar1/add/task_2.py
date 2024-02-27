def greetings(n, ln):
    return f'{n} {ln}, добро пожаловать!'


name = str(input('введите имя '))
last_name = str(input('введите фамилию '))

print(greetings(name, last_name))

