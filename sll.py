# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:
from SLNode import *
class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass
class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)
        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)
    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out
    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length
    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next
    # ------------------------------------------------------------------ #
    def insert_front(self, value: object) -> None:
        """
        TODO: Write this implementation
        creates new node of value, ataches everything after head to this new node and ataches this new node to the head
        """
        newNode = SLNode(value)
        newNode.next = self._head.next
        self._head.next = newNode
        pass
    def insert_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        loops through until it reaches the back and inserts a value as a node at that .next
        """
        index = self._head
        for i in range(self.length()+1):
            if index.next == None:
                index.next = SLNode(value)
                break
            else:
                index = index.next

        pass
    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        indexes through the Linked List till it reaches the specified index and inserts a new value by attaching the end of the LL to the new node and attaching the front of the linked list to the node

        """

        if index < 0 or index > self.length():
            raise SLLException
        cur = self._head
        for i in range(0,index):
            cur = cur.next
        newNode = SLNode(value)
        newNode.next = cur.next
        cur.next = newNode
        pass
    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        tracks through the linked list till it reaches the correct index and then cuts out the middle sections an reattaches the LL
        """
        if index < 0 or index > self.length()-1:
            raise SLLException
        prev = self._head
        cur = self._head
        cur = cur.next
        for i in range(index):
            prev = prev.next
            cur = cur.next
        prev.next = cur.next
        pass
    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        creates 2 indeices/trackers accounts for the base case then iterates through the loop till it reaches the value and snips it, if not it just return true
        """
        prev = self._head
        cur = self._head
        cur = cur.next
        if self.length() == 1 and self._head.next.value == value:
            self._head.next = None
            return True
        while cur != None:
            if cur.value == value:
                prev.next = cur.next
                return True
            prev = prev.next
            cur = cur.next
        return False
        pass
    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        count = 0
        cur = self._head
        while cur != None:
            if cur.value == value:
                count +=1
            cur = cur.next
        return count
        pass
    def find(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        pass
    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        TODO: Write this implementation
        """
        pass
if __name__ == "__main__":
    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)
    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)
    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))
    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")
    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")
    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))
    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)
    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")