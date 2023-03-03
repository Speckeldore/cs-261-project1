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
        """

        return self._heap.length() == 0
    def get_min(self) -> object:
        """
        TODO: Write this implementation
        """
        return self._heap[0]
        pass
    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        """
        min = self._heap[0]
        self._heap[0] = self._heap[self._heap._size-1]
        self._heap._size -= 1
        _percolate_down(self._heap,0)
        return min

        pass
    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """
        pass
    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        return self._heap._size
        pass
    def clear(self) -> None:
        """
        TODO: Write this implementation
        """
        self._heap = DynamicArray()
        pass
def heapsort(da: DynamicArray) -> None:
    """
    TODO: Write this implementation
    """

    pass
# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #
def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    TODO: Write your implementation
    """
    if 2 * parent + 2 > da.length()-1:
        return
    parentVal = da[parent]
    if parentVal > da[2*parent + 2] or parentVal > da[2*parent + 1]:
        if da[2*parent + 2] < da[2*parent + 1]:
            #print("went right", "right:", da[2*parent + 2], "left:",da[2*parent + 1], "parent", da[parent])
            da[parent], da[2*parent + 2] = da[2*parent + 2], da[parent]
            _percolate_down(da,2*parent + 2)
        else:
            #print("went left", "right:", da[2*parent + 2], "left:",da[2*parent + 1], "parent", da[parent])
            #da[2*parent] < da[2*parent + 1]:
            da[parent], da[2*parent + 1] = da[2*parent + 1], da[parent]
            _percolate_down(da, 2*parent + 1)
    pass
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