print("rounding")
print(round(5.5))
for i in range(10):
    print("hi",i)

def hash_function_1(key: str) -> int:
    """Sample Hash function #1 to be used with HashMap implementation"""
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash
def hash_function_2(key: str) -> int:
    """Sample Hash function #2 to be used with HashMap implementation"""
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash
print("------- hash function 1 -------")
lister = ['a','b','c','d','e','f','f']
for i in lister:
    print(hash_function_1(i))
print("------- hash function 2 -------")
lister = ['a','b','c','d','e','f','f']
for i in lister:
    print(hash_function_2(i))
print("------- hash function 3 -------")
for i in range(10):
    print('str' + str(i), i * 100)