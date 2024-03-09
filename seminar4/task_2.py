cnt = ["Andorra", "Belarus", "Denmark", "Kenya", "Jamaica", "Romania"]
fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]

countryIndex = {}

for i in range(len(cnt)):
    countryIndex[cnt[i]] = fh[i]

print(countryIndex)
