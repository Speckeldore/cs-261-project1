N = 10
for i in range(N//2 - 1, -1, -1):
    print(i)
p = 10
for i in reversed(range(0,p//2)):
    print(i)

print("last forloop")
N = 10
for i in range(N-1, 0, -1):
    print(i)


    def prelocate(da,start,end):
        for j in reversed(range(start, end)):
            print(da, "parent:", da[j], "indexJ-start:", j-start)
            _percolate_down2(da, j-start, start)


    for i in range(0, 19):
        start = i
        end = da._size-1
        print("------------prelocation #", i, "start",start, "end",end, "------")
        prelocate(da, start, end)