# Name: Skyler Santos
# OSU Email: santossk@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 2/13/23
# Description: This is the stack made from a dynamic array
from dynamic_array import *
class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass
class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()
    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'
    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()
    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()
    # -----------------------------------------------------------------------
    def push(self, value: object) -> None:
        """
        TODO: Write this implementation
        uses the dynamic array append method to add at the end of the array by using the last index of the array
        """
        self._da.append(value)
        pass
    def pop(self) -> object:
        """
        TODO: Write this implementation
        sets the value at an index to 0
        but also saves the value to be returned using the dynamic array methods
        """
        if self.size() == 0:
            raise StackException
        value = self._da.get_at_index(self.size()-1)
        self._da.remove_at_index(self.size()-1)
        return value
        pass
    def top(self) -> object:
        """
        TODO: Write this implementation
        raises an excpetion if empty
        returns value which is equal to the value at the end of the dynamic array
        which represents the (top)
        """
        if self.size() == 0:
            raise StackException
        value = self._da.get_at_index(self.size()-1)
        return value
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