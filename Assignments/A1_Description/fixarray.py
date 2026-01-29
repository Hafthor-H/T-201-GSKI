import ctypes

class DumbFixedSizeArray:

    """
        Fixed-size array (using the ctypes package to access the underlying C-code interface).
    """

    def __init__(self, capacity: int = 4):
        """
        Creates an array of a fixed size, where each element is an object reference.
        :param capacity: array's capacity/size
        """
        self.initial_capacity = capacity

        if capacity <= 0:
            raise ValueError("FixedSizeArray capacity must be positive")
        self.__capacity = capacity
        self.__array = (ctypes.py_object * self.__capacity)()
        for i in range(self.__capacity):
            self.__array[i] = None   # Strictly speaking, not needed (NULL/None by default)

    def length(self)-> int:
        counter = 0
        for i in self.__array:
            if i is None:
                continue
            counter += 1
        return counter

    def __getitem__(self, index: int):
        """
        Accessing an element at given index (x = A[index]).
        Time complexity: O(n)
        :param index
        :return Element at index (exception if index is out of range)
        """

        if index < 0:
            if index < -(self.__capacity):
                raise IndexError("Index out of range")
            return self.__array[self.length() + index]
        if index >= self.__capacity:
            raise IndexError("Index out of range")
        elif self.__array[index] is None:
            raise IndexError("Nothing there cuh")
        return self.__array[index]

    def double_the_array(self):
        self.__capacity *= 2
        new_array = (ctypes.py_object * self.__capacity)()
        for i in range(self.__capacity):
            new_array[i] = None
        for j, k in enumerate(self.__array):
            new_array[j] = k
        self.__array = new_array

    def append_that_shit(self, value):
        if self.length() == self.__capacity:
            self.double_the_array()
        self.__array[self.length()] = value

    def clear_da_shit(self):
        self.__array = (ctypes.py_object * self.initial_capacity)()
        for i in range(self.initial_capacity):
            self.__array[i] = None


    def __setitem__(self,index: int ,value: object):
        """
        Updating an element at given index (A[index] = x).
        Time complexity: O(1)   O(n)?
        :param index
        :return Element at index (exception if index is out of range)
        """
        if index < 0:
            if index < -(self.__capacity):
                raise IndexError("Index out of range")
            
            self.__array[self.length() + index] = value
        elif index > self.length():
            raise IndexError("Cannot set a value to len +1")

        
        else:
            try:
                self.__array[index] = value
            except IndexError:
                self.double_the_array()
                self.__array[index] = value
    
    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return:
        """
        self.__index = 0
        return self

    def __next__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return the element at index self.__index (exception if out of range)
        """
        if self.__index >= self.capacity():
            raise StopIteration
        elem = self.__array[self.__index]
        self.__index += 1
        return elem

    def capacity(self) -> int:
        """
        Returns the capacity of the array.
        :return: array's capacity
        """

        return self.__capacity

    def __str__(self) -> str:
        string_representation = []
        for i in self.__array:
            if i is None:
                continue
            string_representation.append(str(i))

        return ", ".join(string_representation)
        
    def count(self,value):
        counter = 0
        for i in self.__array:
            if i is value:
                counter += 1
        return counter
    

