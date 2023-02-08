list1 = [1,0]

def inserter(value,index):
    print("value",value, "index",index)

    for i in reversed(range(index,1)):
        print("enters the 4loop")
        list1[i + 1] = list1[i]
        if i == index:
            print("enters the if")
            list1[i] = value
            break

inserter(15,0)

print(list1)

for i in reversed(range(0,1)):
    print(i)