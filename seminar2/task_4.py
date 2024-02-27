from math import log


def log_list(ls):
    return [log(i) for i in ls]


incomes = [10, 20, 40, 123, 234]
loc_inc = log_list(incomes)
print(loc_inc)



