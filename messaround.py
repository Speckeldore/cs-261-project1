da = []
da.append(1)
da.append(2)
print(da[-1])
for i in range(1000000):
    print((i ** 2) % 59, da[-1] + 1)
    if (i**2)%60 == da[-1] + 1:
        print((i**2)%60)
        da.append((i**2)%60)
print(da)