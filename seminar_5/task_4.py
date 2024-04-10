from math import log


def my_log(lst):
    # for n in lst:
    #     print(log(n))

    return [(None if n <= 0 else log(n)) for n in lst]


sample = [1, 3, 2.5, -1, 9, 0, 2.71]


print(my_log(sample))

