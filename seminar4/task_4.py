grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
          'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
          'Ursula': 4, 'Viktor': 5}

excel = []
good = []
satisf = []
bad = []

for key in grades:
    print(f'{key} - {grades[key]}')
    if grades[key] >= 5:
        excel.append(key)
    elif grades[key] == 4:
        good.append(key)
    elif grades[key] == 3:
        satisf.append(key)
    elif grades[key] <= 2:
        bad.append(key)


print(f'excel: {excel}')
print(f'good: {good}')
print(f'satisf: {satisf}')
print(f'bad: {bad}')
