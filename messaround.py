capacity = 2
if capacity == 2 or capacity == 3:
    print("true")
if capacity == 1 or capacity % 2 == 0:
    print("false")
factor = 3
while factor ** 2 <= capacity:
    if capacity % factor == 0:
        print("false")
    factor += 2