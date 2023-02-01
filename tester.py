list = [0,1,2,3,4,5]

def rotate(arr,steps):
    if steps < 0:
        steps = abs(steps)
        for k in range(steps):
            first = arr[0]
            for i in range(len(arr) - 1):
                arr[i] = arr[i + 1]
            arr[len(arr) - 1] = first
        return
    else:
        for k in range(steps):
            last = arr[-1]
            print('last: ',last)
            for i in reversed(range(len(arr)-1)):
                arr[i+1] = arr[i]
            arr[0] = last

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

rotate(list,-3)
print(list)


