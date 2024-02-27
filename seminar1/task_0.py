a = [1, 0, 9, 12, 18, 34, 89, 91, 33, 127]
b = [2, 8, 9, 11, 76, 25, 44]

print('a:', a)
print('b:', b)
print(a[0])
print(a[2])
print(a[-1])

b.append(7)
print('b:', b)

a[4] = 8
print('a:', a)

merged = a + b
print('merged:', merged)

c = a.copy()
c[-1] = 100

print('a:', a)
print('c:', c)



