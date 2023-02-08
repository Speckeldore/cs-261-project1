def reduce(self, reduce_func, initializer=None) -> object:
    #cas for returning just the initializer; there is no array
    if self._size == 0:
        return initializer
    #This is the case for there is only 1 element in the array
    #if self._size == 1 and initializer is not None:
    #    return reduce_func(initializer, self._data[0])
    for i in range(0, self._size):
        if initializer == None:
            initializer = self._data[0]
            i+=1
            if self._size == 1:
                return reduce_func(self._data[0], 0)
        value = reduce_func(initializer, self._data[i])
        initializer = value

    return value