# Name: Skyler Santos
# OSU Email: santossk@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2
# Due Date: 2/6/23
# Description: Dynamic Array and its functions
from static_array import StaticArray
class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass
class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)
        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)
    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'
    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self
    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration
        self._index += 1
        return value
    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]
    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value
    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)
    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)
    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def magic(self) -> None:
        for i in range(self._size - 1, -1, -1):
            self.append(self._data[i])
            self.remove_at_index(i)

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size
    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity
    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")
    # -----------------------------------------------------------------------
    def resize(self, new_capacity: int) -> None:
        """
        TODO: Write this implementation
        """
        if new_capacity < 1 or new_capacity < self._size:
            return
        self._capacity = new_capacity
        newArr = StaticArray(self._capacity)
        for value in range(0, self._size):
            newArr.set(value, self._data[value])
        self._data = newArr

    def append(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if self._size == self._capacity:
            self.resize(2*self._capacity)
        self._data[self._size] =  value
        self._size = self._size + 1


    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if self._size == self._capacity:
            self.resize(2*self._capacity)
        if index < 0 or index > self._size:
            raise DynamicArrayException
        if self._size == 0:
            self._data[0] = value
        if index == self._size:
            self._data[index] = value

        self._size += 1
        for i in reversed(range(index,self._size-1)):
            self._data[i+1] = self._data[i]
            if i == index:
                self._data.set(i,value)
                return

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0 or index > self._size -1:
            raise DynamicArrayException
        if self._size < (1/4)*self._capacity and self._capacity >10 :
            self.resize(2 * self._size)
            if (2)*self._size < 10:
                self.resize(10)

        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._size -= 1

        pass
    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        TODO: Write this implementation
        """
        if start_index + size > self._size or size < 0:
            raise DynamicArrayException
        if start_index < 0 or self._size == 0:
            raise DynamicArrayException
        if start_index < self._size and start_index >= 0:
            narr = DynamicArray()
            narrind = 0
            for i in range(start_index, start_index + size):
                narr.append(self._data[i])
                narrind += 1
        else:
            raise DynamicArrayException
        return narr
        pass
    def merge(self, second_da: "DynamicArray") -> None:
        """
        TODO: Write this implementation
        """

        for i in range(0,second_da._size):
            self.append(second_da[i])

        pass
    def map(self, map_func) -> "DynamicArray":
        """
        TODO: Write this implementation
        """
        narr = DynamicArray()
        for i in range(0,self._size):
             narr.append(map_func(self._data[i]))
        return narr
        pass
    def filter(self, filter_func) -> "DynamicArray":
        """
        TODO: Write this implementation
        """
        narr = DynamicArray()
        for i in range(0, self._size):
            if filter_func(self._data[i]) == True:
                narr.append(self._data[i])
        return narr
        pass
    def reduce(self, reduce_func, initializer=None) -> object:
        """
        TODO: Write this implementation
        """
        # if there is no array return initializer
        if self._size == 0:
            return initializer
        # if the intializer is none and and the size of the array is 1
        if initializer == None:
            if self._size == 1:
                return self._data[0]
            value = self._data[0]
        # if the initializer is a value
        if initializer is not None:
            value = initializer
            value = reduce_func(value, self._data[0])

        for i in range(1, self._size):
            value = reduce_func(value, self._data[i])

        return value
def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    TODO: Write this implementation
    """
    modarr = DynamicArray()
    if arr.length() == 1:
        modarr.append(arr[0])
        return (modarr, 1)

    modcount = 1
    counter = 1
    currentcount = 1
    indice = 0
    for i in range(0, arr.length()-1):

        if arr[i] == arr[i+1]:
            counter += 1
            continue

        else:
            # if this isnt bigger than the current identifed mode
            if currentcount > counter:
                counter = 1
                continue
            # if this new coutned number is bigger than the previosuly identified mode
            if currentcount < counter:
                currentcount = counter
                modarr = DynamicArray()
                modarr.append(arr[i])
                counter = 1
            # if this new counted number is the same as the previously identified mode
            if currentcount == counter:
                modarr.append(arr[i])
                counter = 1
    if currentcount == counter:
        modarr.append(arr[i+1])
    if currentcount < counter:
        modarr = DynamicArray()
        modarr.append(arr[i+1])
        currentcount = counter
    return (modarr, currentcount)
    pass
# ------------------- BASIC TESTING -----------------------------------------
if __name__ == "__main__":
    print("\n# resize - example 1")
    da = DynamicArray()
    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()
    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)
    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)
    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)
    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())
    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)
    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)
    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)
    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)
    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)
    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())
    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())
    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)
    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")
    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")
    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)
    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)
    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))
    print("\n# map example 2")
    def double(value):
        return value * 2
    def square(value):
        return value ** 2
    def cube(value):
        return value ** 3
    def plus_one(value):
        return value + 1
    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))
    print("\n# filter example 1")
    def filter_a(e):
        return e > 10
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))
    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length
    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))
    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))
    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )
    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")
    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
    print("All new test: SKYLERS test")
    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
    print("BEFORE")
    print(da)
    da.magic()
    print("BEFORE2")
    print(da)
    da.insert_at_index(1,255)
    print(da)