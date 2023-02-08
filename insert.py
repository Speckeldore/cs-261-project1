def reduce(self, reduce_func, initializer=None) -> object:
    """
    TODO: Write this implementation
    """
# if there is no array return initializer
    if self._size == 0:
        return initializer
#if the intializer is none and and the size of the array is 1
    if initializer == None:
        if self._size == 1:
            return self._data[0]
        value = self._data[0]
#if the initializer is a value
    if initializer is not None:
        value = initializer
        value = reduce_func(value, self._data[0])

    for i in range(1, self._size):
        value = reduce_func(value, self._data[i])

    return value