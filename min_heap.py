# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:
from dynamic_array import *
class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass
class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()
        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)
    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)
    def add(self, node: object) -> None:
        """
        TODO: Write this implementation
        appends the value
        if it is greater than the root node it goes to the child compares and continues till it reaches its leaf spot
        """
        self._heap.append(node)
        ci = self._heap._size -1
        child = node
        pi = int((self._heap._size -1 - 1) / 2)
        if pi < 0:
            return
        else:
            parent = self._heap[pi]
        while parent > child:
            self._heap[pi] = child
            self._heap[ci] = parent
            cis = pi
            ci = pi
            pi = int((cis - 1) / 2)

            if pi < 0:
                break
            child = self._heap[ci]
            parent = self._heap[pi]

        pass
    def is_empty(self) -> bool:
        """
        TODO: Write this implementation
        if the length is 0 it will return false
        """

        return self._heap.length() == 0
    def get_min(self) -> object:
        """
        TODO: Write this implementation
        returns the value at the first index of the heap
        """
        #hehe
        try:
            return self._heap[0]
        except:
            raise MinHeapException
    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        trys to remove the first value of the heap
        it then rotates the last value in decrements the size and percolates that value down
        """
        try:
            min = self._heap[0]
            self._heap[0] = self._heap[self._heap._size-1]
            self._heap._size -= 1
            _percolate_down(self._heap,0)
            return min
        except:
            raise MinHeapException

        pass
    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        uses the percolate down to reorganize the current structure nodes
        it then adds in the values to the actual heap self._heap
        """
        self.clear()
        for i in reversed(range(0, da._size // 2)):
            _percolate_down(da, i)
        for i in da:
            self._heap.append(i)
        pass
    def size(self) -> int:
        """
        TODO: Write this implementation
        returns the intrisic value of size
        """
        return self._heap._size
        pass
    def clear(self) -> None:
        """
        clears the current array by pointing to a new dynamic array that is empty
        TODO: Write this implementation
        """
        self._heap = DynamicArray()
        pass
def heapsort(da: DynamicArray) -> None:
    """
    uses the prelocate to prelocate smaller vallues to the end
    TODO: Write this implementation
    it starts by organizing the dynamic array into a reverse heap
    after it switches each consecutive value and then prelocates the value down if it is smaller
    """
    for i in reversed(range(0,da._size//2)):
        _prelocate_down3(da,da._size, i)
        #print("after prelocation3d",da)
    for j in reversed(range(0,da._size)):
        da[j], da[0] = da[0], da[j]
        _prelocate_down3(da,j,0)











    pass
# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #
def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    TODO: Write your implementation
    compares which value is smaller and switches the smaller value to the current index and then recurivley jumps forward through the child nodes
    """
    if 2 * parent + 2 > da.length()-1:
        if 2 * parent + 1 == da.length()-1:
            if da[parent] > da[2 * parent + 1]:
                da[parent], da[2 * parent + 1] = da[2*parent + 1], da[parent]
        return
    parentVal = da[parent]
    if parentVal > da[2*parent + 2] or parentVal > da[2*parent + 1]:
        'Swap right'
        if da[2*parent + 2] < da[2*parent + 1]:
            #print("went right")
            #print("went right", "right:", da[2*parent + 2], "left:",da[2*parent + 1], "parent", da[parent])
            da[parent], da[2*parent + 2] = da[2*parent + 2], da[parent]
            _percolate_down(da,2*parent + 2)
        else:
            #print("went left")
            #print("went left", "right:", da[2*parent + 2], "left:",da[2*parent + 1], "parent", da[parent])
            #da[2*parent] < da[2*parent + 1]:
            da[parent], da[2*parent + 1] = da[2*parent + 1], da[parent]
            _percolate_down(da, 2*parent + 1)
    pass
def _percolate_down2(da: DynamicArray, parent: int, start) -> None:
    """
    TODO: Write your implementation
    2nd version of prelocate that prelocates small values down
    """
    if start == None:
        start = 0
    r = 2 * parent + 2 + start
    l = 2 * parent + 1 + start
    print('l', l, 'r', r, 'parent', parent + start)
    if r > da.length()-1:
        if l == da.length()-1:
            print("parent", da[parent+start], "left", da[l])
            if da[parent+start] < da[l]:
                da[parent+start], da[l] = da[l], da[parent+start]
        return
    print("parent", da[parent+start], "right", da[r], "left", da[l])
    parentVal = da[parent+start]
    if parentVal < da[r] or parentVal < da[l]:
        'Swap right'
        if da[r] > da[l]:
            #print("went right")
            #print("went right", "right:", da[2*parent + 2], "left:",da[2*parent + 1], "parent", da[parent])
            da[parent+start], da[r] = da[r], da[parent+start]
            _percolate_down2(da,r-start,start)
        else:
            #print("went left")
            #print("went left", "right:", da[2*parent + 2], "left:",da[2*parent + 1], "parent", da[parent])
            #da[2*parent] < da[2*parent + 1]:
            da[parent+start], da[l] = da[l], da[parent+start]
            _percolate_down2(da,l-start,start)
    pass
def _prelocate_down3(da: DynamicArray,size: int, parent: int) -> None:
    "3rd prelocate it prelocates smaller value down and takes in the root like the previous prelocator"
    big = parent
    l = 2*parent+1
    r = 2*parent+2
    switched = False
    #if r < size or l < size:
        #if r < size:
            #big = r,switched = True
        #if l< size:
    if r < size:
        if da[big] > da[r]:
            big = r
            switched = True
    if l < size:
        if da[big] > da[l]:
            big = l
            switched = True
    if switched == True:
        da[parent],da[big] = da[big],da[parent]
        #da[parent], da[2 * parent + 1] = da[2 * parent + 1], da[parent]
        (da,size,big)

# ------------------- BASIC TESTING -----------------------------------------
if __name__ == '__main__':
    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)
    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)
    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())
    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())
    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())
    print("\nPDF - remove_min example Skyler")
    h = MinHeap([8,9,10])
    print(h.remove_min())

    print("h after removeing the min",h)
    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())
    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da = DynamicArray([90943, -41284, -3100, -73248])
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)
    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")
    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
    print("\nPDF - heapsort example 2")
    print("------------------------")
    print("\nPDF - heapsort example 3")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300, 301, 40, 25, 20, 65, 78, 88, 94, 82, 1004, 500, 60])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())
    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())
    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)