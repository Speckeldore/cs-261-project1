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
print(hash_function_1('key915')%10,hash_function_2('key915')%10)
print(5/3)
print((5/3)>1)