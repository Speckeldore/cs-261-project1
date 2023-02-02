

def rotate(arr,steps):
    narr = StaticArray(arr.length())
    for i in range(arr.length):
        narr[i] = arr[i]
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








    narr = StaticArray(arr.length())

    def rightRotateByOne(A, N):
        last = A[A.length()-1]
        for i in reversed(range(A.length() - 1)):
            N[i + 1] = A[i]

        A[0] = last

    def leftRotateByOne(A, N):
        first = A[0]
        for i in range(A.length() - 1):
            N[i] = A[i + 1]
        N[A.length() - 1] = first

    if steps < 0:
        steps = abs(steps)
        if steps / arr.length() > 1.0:
            steps = steps % arr.length()
        for i in range(steps):
            if i > 1:
                leftRotateByOne(narr, narr)
                continue
            rightRotateByOne(arr, narr)
    if steps > 0:
        steps = abs(steps)
        if steps / arr.length() > 1.0:
            steps = steps % arr.length()
        for i in range(steps):
            if i > 1:
                leftRotateByOne(narr, narr)
                continue
            leftRotateByOne(arr, narr)
    if steps == 0:
        for i in range(arr.length()):
            narr[i] = arr[i]
    return narr


