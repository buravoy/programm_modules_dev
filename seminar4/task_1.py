rept = {
    "python": "питон",
    "anaconda": "анаконда",
    "tortoize": "черепаха"
}
print(rept)

rept['snake'] = 'змея'
print(rept)

rept['tortoise'] = rept.pop('tortoize')
print(rept)

for key in rept:
    print(f'{rept[key]} по-английски будет {key}.')
