# Напишите функцию binom_prob(), которая считает вероятность того, что проведя n испытаний
# Бернулли с вероятностью успеха p, мы получим ровно k успехов. Эта функция принимает на вход три
# аргумента: p, n и k и возвращает такой результат:
# Для расчета биномиального коэффициента можно использовать функцию, написанную на лекции


def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f


def binom(k, n):  # вычисляет биномиальные коэффициенты из эн по ка
    return factorial(n) // (factorial(k) * factorial(n - k))


# можно использовать целочисленное деление, поскольку результат гарантированно целы
def binom_prob(p, n, k):  # считает вероятность того, что проведя n испытаний Бернулли с вероятностью успеха p, мы получим ровно k успехов
    return binom(k, n) * (p ** k) * ((1 - p) ** (n - k))
