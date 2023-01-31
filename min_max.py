import random
from static_array import *

def min_max(arr: StaticArray) -> (int, int):
    """
    TODO: Write this implementation
    """
    for i in range(arr.length()):
        print(i)
        print(arr[i])
    #my_tuple = (min,max)
    #return my_tuple


arr1 = StaticArray(5)
for i, value in enumerate([7, 8, 6, -5, 4]):
    arr[i] = value
min_max(arr1)
print('here',arr1[0])