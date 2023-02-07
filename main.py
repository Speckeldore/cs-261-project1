from static_array import StaticArray, StaticArrayException

class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    """
    pass

class Dynamic_Array:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        """
        self.size = 0
        self.capacity = 10
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self):
        return str(self.data)

    def __iter__(self):
        """
        Create iterator for loop
        """
        self._index = 0

        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        """
        try:
            value = self.data[self._index]
        except StaticArrayException:
            raise StopIteration

        self._index = self._index + 1
        return value

    # Will need to be amended to check if there is room and call function to expand array when necessary
    def append(self, val):
        if self.size == self.capacity:
            self.resize(1)
        self.data[self.size] =  val
        self.size = self.size + 1

    # Add a function that will create an expanded array with twice the size with the same elements
    def resize(self, new_capacity: int) -> None:
        """
        TODO: Write this implementation
        """
        self.capacity = self.capacity + new_capacity
        newArr = StaticArray(self.capacity)
        for value in range(0,self.size):
            newArr.set(value,self.data[value])
        self.data = newArr
        pass


# Create new instance of Dynamic_Array
my_list = Dynamic_Array()

# Build list with 10 items
for i in range(10):
    my_list.append(i)
my_list.append(5)
# Iterate through list automagically via iterator
for value in my_list:
    print(value)

print(my_list)