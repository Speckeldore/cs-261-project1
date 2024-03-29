# Name: Skyler Santos
# OSU Email: santossk@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: 3/17
# Description: Hash map with linked lists for collisions
from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)
class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()
        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())
        self._hash_function = function
        self._size = 0
    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out
    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1
        while not self._is_prime(capacity):
            capacity += 2
        return capacity
    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True
        if capacity == 1 or capacity % 2 == 0:
            return False
        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2
        return True
    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size
    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity
    # ------------------------------------------------------------------ #
    def put(self, key: str, value: object) -> None:
        """
        TODO: Write this implementation
        This method updates the key/value pair in the hash map
        it resizes if neccesary
        it then targets the deisignated linked list and the it either updates the value or inserts a new one
        """
        #simply adding the value
        loadF = self._size / self._capacity
        if loadF >= 1:
            self.resize_table(2 * self._capacity)

        LL = self._buckets.get_at_index(self._hash_function(key)%self._capacity)
        # If the given key already exists in the hash map, its associated value must be replaced with the new value
        if LL.contains(key) is not None:
            LL.contains(key).value = value
        else:
            LL.insert(key,value)
            self._size += 1
        # If the given key is not in the hash map, a new key/value pair must be added.
        # if load factor is greater than 1 double size to next prime number?
            #for _ in range(self._capacity):
                #self._buckets.append(LinkedList())

        pass
    def empty_buckets(self) -> int:
        """
        TODO: Write this implementation
        it counts the linked lists that have no length
        """
        emp = 0
        for i in range(self._capacity):
            if self._buckets[i].length() == 0:
                emp +=1
        return emp

    def table_load(self) -> float:
        """
        TODO: Write this implementation
        simply calculates these variables deivided and returns it
        """
        return self._size/self._capacity

    def clear(self) -> None:
        """
        TODO: Write this implementation
        creates a new dynamic area for vairbale buckets resets size to 0 and then it appends Linked lists so
        that the capcity is still the same
        """
        self._buckets = DynamicArray()
        self._size = 0
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

    def resize_table(self, new_capacity: int) -> None:
        """
        TODO: Write this implementation
        checks to see if new capcity is prime
        saves the old dynamic array and rehashes these values into the new array self._buckets
        """''
        if new_capacity < 1:
            return
        if self._is_prime(new_capacity) is False:
            new_capacity = self._next_prime(new_capacity)

        old_buckets = self._buckets
        self._capacity = new_capacity
        self.clear()

        for i in range(old_buckets.length()):
            a = old_buckets[i]
            for j in a:
                self.put(j.key,j.value)
        pass
    def get(self, key: str):
        """
        TODO: Write this implementation
        if the value for that key exist it returns the value
        """

        LL = self._buckets[self._hash_function(key)%self._capacity]
        if LL.contains(key) is not None:
            return LL.contains(key).value
        pass
    def contains_key(self, key: str) -> bool:
        """
        TODO: Write this implementation
        checkt to see if the deisgnated linked list contains the actual input key
        """
        LL = self._buckets[self._hash_function(key) % self._capacity]
        if LL.contains(key) != None:
            return True
        else:
            return False



        pass
    def remove(self, key: str) -> None:
        """
        TODO: Write this implementation
        if the linked list of designates key existed the value is removed and sice is decremented
        """
        LL = self._buckets[self._hash_function(key)%self._capacity]
        if LL.contains(key) is not None:
            LL.remove(key)
            self._size -= 1
        pass
    def get_keys_and_values(self) -> DynamicArray:
        """
        TODO: Write this implementation
        gathers the key value pair as a tuple and appends it to a new array that will be returned
        """
        DA = DynamicArray()
        for i in range(self._capacity):
            a = self._buckets[i]
            for j in a:
                DA.append((j.key,j.value))
        return DA
        pass
def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    TODO: Write this implementation
    as it puts values into a hash map it uses the
    the actual value number as a key and its value becomes the frequency
    we compare each value we put into the hashmap against our current mode
    and update it if neccesary
    """
    # if you'd like to use a hash map,
    # use this instance of your Separate Chaining HashMap
    bigVal = DynamicArray()
    #bigVal.append(0)
    bigTup = (bigVal,1)
    map = HashMap(da.length())
    for i in range(da.length()):
        i = da[i]
        if map.contains_key(i):
            freq = map.get(i) + 1
            if bigTup[1] == freq:
                bigTup[0].append(i)
            if bigTup[1] < freq:
                bigVal = DynamicArray()
                bigVal.append(i)
                bigTup = (bigVal,freq)
            map.put(i,freq)
        else:
            map.put(i,1)
        if bigTup[1] == 1:
            bigTup[0].append(i)
    return bigTup
# ------------------- BASIC TESTING ---------------------------------------- #
if __name__ == "__main__":
    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(),m.get_capacity())
    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(),
m.get_capacity())
    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())
    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))
    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())
    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())
    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())
    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(23, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)
        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')
        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(),
round(m.table_load(), 2))
    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))
    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)
    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(53, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))
    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)
    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')
    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())
    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
    print(m.get_keys_and_values())
    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")
    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu",
"Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )
    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")