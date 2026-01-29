from fixarray_template import FixedSizeArray
import collections
from collections.abc import Iterable
import ctypes



class DAList:
    """
    -Dynamic array (mimicking most of Python's list behavior).
    """

    ##############################################################################################################
    # Part 1 section
    ##############################################################################################################

    def __init__(self, capacity: int = 4):
        """
        Constructor
        Time complexity: O(1)
        :param capacity:
        """
        self.data = FixedSizeArray(capacity)
        self.capacity = self.data.capacity()


    def __len__(self) -> int:
        """
        Returns the number of elements in the array ( ... = len(A))
        Time Complexity: O(n)
        :return: number of elements
        """
        counter = 0
        for i in self.data:
            if i is None:
                continue
            counter += 1
        return counter
    

    def __getitem__(self, index: int):
        """
        Accessing an element at given index (... = A[index]).
        Time complexity: O(n)
        :param index
        :return Element at index (exception if index is out of range)
        """

        if index >= len(self):
            raise IndexError("Index out of range")
        elif index < 0:
            return self.data[len(self) + index]
        elif self.data[index] is None:
            raise IndexError("Nothing there cuh")
        return self.data[index]
    
    def __setitem__(self, index: int ,value: object):
        """
        Updating an element at given index (A[index] = value).
        Time complexity: O(n)
        :param index:
        """

        if index < 0:
            if index < -(len(self)):
                raise IndexError("Index out of range")
            self.data[len(self) + index] = value
        elif index > len(self):
            raise IndexError("Cannot set a value to len +1")

        
        else:
            try:
                self.data[index] = value
            except IndexError:
                self.double_the_array()
                self.data[index] = value


        return self.data.__setitem__(index, value)
    

    def double_the_array(self)->None:
        '''
        Doubles the capacity of the array
        time complexity: O(n)
        '''
        self.capacity *= 2
        new_array = (ctypes.py_object * self.capacity)()
        for i in range(self.capacity):
            new_array[i] = None
        for j, k in enumerate(self.data):
            new_array[j] = k
        self.data = new_array

    def __str__(self):
        """
        Returns a string representation of the array, e.g, [1, 2, 3] (str(A))
        Time complexity: O(n^2)
        :return: string representation
        """

        return "[" + ", ".join(str(x) for x in self) + "]"

    def __delitem__(self, index: int):
        """
        Delete an element at given index (del A[index]).
        Time complexity: O(n^2)
        :param index
        """
        for i in range(index, len(self) - 1):
            self.data[i] = self.data[i + 1]
        self.data[len(self) - 1] = None

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: O(1)
        :return self
        """
        self.__index = 0
        return self

    def __next__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: O(n)
        :return the element at index self.__index (exception if out of range)
        """
        if self.__index >= len(self):
            raise StopIteration
        elem = self.data[self.__index]
        self.__index += 1
        return elem

    def clear(self):
        """
        Clears the array. Ensure you clear the references to the cleared object (such that the garbage collector
        can reclaim them).
        Time complexity: O(n)
        """
        self.data = (ctypes.py_object * self.capacity)()
        for i in range(self.capacity):
            self.data[i] = None

    def count(self, value: object):
        """
        Counts the number of times an element 'value' appears in the list.
        Time complexity: O(n)
        :return: number of times value appears
        """
        counter = 0
        for i in self.data:
            if i is value:
                counter += 1
        return counter
    

    def index(self, value: object):
        """
        Returns the index of the first occurrence of element 'value' in the array, or raises ValueError if not found.
        Time complexity: O(n^2)
        :param value: The value to look for
        :return:  index of first occurrence in list
        """
        for i in range(len(self)):
            if self.data[i] == value:
                return i
        raise ValueError(f"{value} is not in list")


    def insert(self, index: int, value: object):
        """
        Inserts the element 'value' at position index in the array (shifting the subsequent items).
        Time complexity: O(n)
        :param index: position where to append the element.
        :param value: element to append
        """
        if index > len(self):
            raise IndexError("Index out of range")
        elif len(self) == self.capacity:
            self.double_the_array()

        for i in range(len(self), index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value

    def reverse(self):
        """
        Reverses the array 'in place', e.g. [1, 2, 3] becomes [3, 2, 1].
        Time complexity: O(n^2)
        """
        temp_array = DAList(self.capacity)

        counter = 0
        
        for i in range(1,self.capacity+1):
            if self.data[-i] is None:
                continue

            temp_array[counter] = self.data[-i]
            counter += 1
        
        self.data = temp_array.data
        return self
    ##############################################################################################################
    # Part 2 section
    ##############################################################################################################

    def append(self, value: object):
        """
        Appends the element 'value' to the end of the array. Doubles the capacity of the array
        if it is already full before inserting an element.
        Time complexity: O(n)
        :param value: element to append
        """
        if len(self) == self.capacity:
            self.double_the_array()
        self.data[len(self)] = value

    def copy(self):
        """
        Returns a shallow copy of the array.
        Time complexity: O(n^2)
        :return: copy of array
        """
        copied_list = DAList()

        for i in range(len(self)):
            
            copied_list[i] = self.data[i]
            
        return copied_list
            


    def extend(self, iterable: collections.abc.Iterable):
        """
        Extends the array with the elements from iterable.
        Time complexity: O(n^2)
        :param iterable: An iterable object (e.g., a list)
        """
        for i in iterable:
            self.append(i)

    def pop(self, index: int):
        """
        Remove the element at a given index from the array
        Time complexity: O(n)
        :param index: position of element to remove
        """

        value = self.data[index]
        self.remove(value)
        return value


    def remove(self, value: object):
        """
        Removes the first occurrence of element 'value' in the array, or raises ValueError if not found.
        Time complexity: O(n^2)
        :param value: The value to remove
        """
        for i in range(self.__len__()):
            if self.data[i] == value:
                self.__delitem__(i)
                return
            
        raise ValueError(f"{value} is not in list")


