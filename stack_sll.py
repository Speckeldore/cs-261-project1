# Name: Skyler Santos
# OSU Email: santossk@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 2/13/23
# Description: made a stack from individual SLnodes
from SLNode import SLNode
class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass
class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
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
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None
    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length
    # -----------------------------------------------------------------------
    def push(self, value: object) -> None:
        """
        TODO: Write this implementation
        holds a case for if this stack is empty
        if not is saves the previous chain
        sets the head to a new node of value and attaches the chain to the head.next
        """
        if self._head == None:
            self._head = SLNode(value)
            return

        prev = self._head
        self._head = SLNode(value)
        self._head.next = prev
        pass
    def pop(self) -> object:
        """
        TODO: Write this implementation
        checks if the stack is empty else it saves the value
        iterates the head and returns the saved value
        """
        if self._head == None:
            raise StackException
        value = self._head.value
        self._head = self._head.next
        return value
        pass
    def top(self) -> object:
        """
        TODO: Write this implementation
        Checks for empty and returns the value seen at head
        """
        if self._head == None:
            raise StackException
        return self._head.value
        pass
# ------------------- BASIC TESTING -----------------------------------------
if __name__ == "__main__":
    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)
    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))
    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)