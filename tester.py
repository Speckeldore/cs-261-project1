list = [0,1,2,3,4,5]

def rotate(arr,steps):
    if steps <= 0 :
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

rotate(list,6)
print(list)