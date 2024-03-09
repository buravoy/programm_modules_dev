pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]
calc = {}

for pair in pairs:
    calc[pair] = pair[0] * pair[1]

print(calc)
