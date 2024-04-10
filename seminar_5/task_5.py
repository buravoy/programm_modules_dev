def make_dictionary(names, ages):
    if len(names) != len(ages):
        print('Списки имеют разную длину')
        return {}
    else:
        return dict(zip(names, ages))


n1 = ["Ann", "Tim", "Sam"]
a1 = [12, 23, 17]

n2 = ["Ann", "Tim", "Sam"]
a2 = [12, 23, 17, 45]

print(make_dictionary(n1, a1))
print(make_dictionary(n2, a2))
