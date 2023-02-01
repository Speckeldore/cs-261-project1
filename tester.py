list = [0,1,2,3,4,5]

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    narr = arr
    if steps == 0:
        return narr
    if steps < 0:
        steps = abs(steps)
        for k in range(steps):
            first = narr[0]
            for i in range(narr.length() - 1):
                narr[i] = narr[i + 1]
            narr[narr.length() - 1] = first
        return narr
    else:
        for k in range(steps):
            last = narr[narr.length()-1]

            for i in reversed(range(narr.length() - 1)):
                narr[i + 1] = narr[i]
            narr[0] = last
    return narr

def rightRotateByOne(A):
    last = A[-1]
    for i in reversed(range(len(A) - 1)):
        A[i + 1] = A[i]

    A[0] = last
def leftRotateByOne(A):
    first = A[0]
    for i in range(len(A)-1):
        A[i] = A[i+1]
    A[len(A)-1] = first

print(range(0,3))

for i in range(0,3):
    print(i)


