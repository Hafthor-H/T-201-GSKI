from collections.abc import Iterable
from fixarray import FixedSizeArray

class DAList:
    """
    Dynamic array (mimicking most of Python's list behavior).
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
        self.capacity = capacity
        self.size = self.capacity
        self.data = FixedSizeArray(self.capacity)

    def __len__(self) -> int:
        """
        Returns the number of elements in the array ( ... = len(A))
        Time Complexity: O(n)
        :return: number of elements
        """
        # count the number of elements in the array and return the result
        return self.data.length()

    def __getitem__(self, index: int):
        """
        Accessing an element at given index (... = A[index]).
        Time complexity: o(1)
        :param index
        :return Element at index (exception if index is out of range)
        """
        # return the element
        return self.data[index]

    def __setitem__(self, index: int, value: object):
        """
        Updating an element at given index (A[index] = value).
        Time complexity: o(n)
        :param index:
        """
        # set the element at the correct index to the value
        self.data.__setitem__(index,value)

    def __str__(self):
        """
        Returns a string representation of the array, e.g, [1, 2, 3] (str(A))
        Time complexity: o(1)
        :return: string representation
        """
        # create a comma separated string of all the elements
        elements_str = ''
        for elem in self.data:
            elements_str += str(elem) + ', '
        # add the brackets and return it
        return '[' + elements_str + ']'

    def __delitem__(self, index: int):
        """
        Delete an element at given index (del A[index]).
        Time complexity: ?
        :param index
        """
        # clear the element at the index
        self.data[index] = None

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: ?
        :return self
        """
        return self

    def __next__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: ?
        :return the element at index self.__index (exception if out of range)
        """
        # return the element at index self.index
        return self.data[self.index]

    def clear(self):
        """
        Clears the array. Ensure you clear the references to the cleared object (such that the garbage collector
        can reclaim them).
        Time complexity: ?
        """
        # clear each element in the array
        for i in range(self.capacity):
            self.data[i] = None

    def count(self, value: object):
        """
        Counts the number of times an element 'value' appears in the list.
        Time complexity: ?
        :return: number of times value appears
        """
        # count the number of 
        counted = 0
        for i in range(self.capacity):
            if self.data[i] != None:
                counted += 1
        return counted

    def index(self, value: object):
        """
        Returns the index of the first occurrence of element 'value' in the array, or raises ValueError if not found.
        Time complexity: ?
        :param value: The value to look for
        :return:  index of first occurrence in list
        """
        # compare each element of the array to the value, if they are the same then
        # return the element's index
        for i in range(self.size):
            elem = self.data[i]
            if elem != value:
                raise ValueError(f"{value} is not in list")
            else:
                return i

    def insert(self, index: int, value: object):
        """
        Inserts the element 'value' at position index in the array (shifting the subsequent items).
        Time complexity: ?
        :param index: position where to append the element.
        :param value: element to append
        """
        # first check if we need to resize the array. If so, resize it
        if not self.size <= self.capacity:
            new_capacity = self.capacity * 2
            new_arr = FixedSizeArray(new_capacity)
            # copy elements from old array to new array
            for i in range(new_capacity):
                new_arr[i] = self.data[i]
            # overwrite old array with new one
            self.data = new_arr
        
        # insert the value, and then shift all other elements in the array to the right 
        # by one to make room for it
        self.data[index] = value
        for i in range(index, self.size):
            self.data[i + 1] = self.data[i]

    def reverse(self):
        """
        Reverses the array 'in place', e.g. [1, 2, 3] becomes [3, 2, 1].
        Time complexity: ?
        """
        # swap each pair of elements about the center index, i.e:
        # 
        #        |               v-----|-----v            v--|--v
        # [1, 2, 3, 4, 5]  -->  [5, 2, 3, 4, 1]  -->  [5, 4, 3, 2, 1]  --> done!
        
        for i in range(self.capacity):
            # first copy the elements
            left_elem = self.data[i]
            right_elem = self.data[len(self) - i]
            # then swap them
            self.data[i] = right_elem
            self.data[len(self) - i] = left_elem
