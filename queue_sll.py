# Name: Skyler Santos
# OSU Email: santossk@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 2/13/23
# Description: This is the Queue made out of SL Node chain
from SLNode import SLNode
class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass
class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None
    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'
    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None
    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length
    # -----------------------------------------------------------------------
    def enqueue(self, value: object) -> None:
        """
        TODO: Write this implementation
        This method has cases for an empty stack and for only having 1 value in the stack
        if those cases arent met then
        it adds on to the existing stack and iterates the self._tail
        """
        if self._head == None:
            self._head = SLNode(value)
            return
        if self._tail == None:
            self._tail = SLNode(value)
            self._head.next = self._tail
            return
        self._tail.next = SLNode(value)
        self._tail = self._tail.next




        pass
    def dequeue(self) -> object:
        """
        TODO: Write this implementation
        this checks for an empty array, and an array with 1 element
        also if the head and tail element are pointing at the same object
        then it returns that value and resets head and tail to None
        """
        if self._tail == None and self._head == None:
            raise QueueException
            return
        if self._tail == None:
            value = self._head.value
            self._head = None
            return value
        if self._head == self._tail:
            value = self._head.value
            self._head = None
            self._tail = None
            return value
        value = self._head.value
        self._head = self._head.next
        return value


        pass
    def front(self) -> object:
        """
        TODO: Write this implementation
        Raises exception if empty and if not returns the head value
        """
        if self._head == None:
            raise QueueException
            return
        return self._head.value
        pass
# ------------------- BASIC TESTING -----------------------------------------
if __name__ == "__main__":
    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)