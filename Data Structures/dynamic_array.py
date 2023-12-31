import ctypes
import logging
logging.basicConfig(level=logging.INFO)

class IllegalArgumentException(Exception):
    """Used for raising exceptions when the capacity of array is negative."""
    pass

class DynamicArray(object):
    """An implementation of a dynamic array in python."""
    def __init__(self):
        self._len = 0 # Apparent size of the array
        self._capacity = 1 # actual size of the array
        self._arr = self._make_array(self._capacity)
        self._index = 0 # keeps track of the index for the iterator

    def _make_array(self, capacity):
        """Creates an array of size `capacity` """
        if capacity<0:
            raise IllegalArgumentException("Invalid capacity")
        return (capacity*ctypes.py_object)()
    
    def __sizeof__(self) -> int:
        return self._len
    
    def isEmpty(self) -> bool:
        """Checks if the array is empty"""
        return self._len == 0
    
    def get(self,index : int):
        """Returns the element at index"""
        if index>=self._len or index<0:
            raise IndexError("Index out of range")
        else:
            return self._arr[index]
    
    def set(self, index : int, value):
        """Inserts value at index"""
        if index>=self._len or index<0:
            raise IndexError("Index out of range")
        else:
            self._arr[index] = value
    
    def append(self, value):
        """Adds value to the end of the array"""
        if self._len+1 > self._capacity:
            # The capacity of the array has been exceeded, create a new array that is double in size
            self._capacity *= 2
            new_array  = self._make_array(self._capacity)
            # Copy the values from the old to new array
            for i in range(self._len):
                new_array[i] = self._arr[i]
            self._arr = new_array
            
        # Add the new value to the end of the array
        self._arr[self._len] = value
        self._len += 1

    def clear(self):
        """Clears the values of the array"""
        for i in range(self._len):
            self._arr[i] = None
        self._len = 0

    def removeAt(self, index):
        """Removes a value ar a specific index"""
        # Check if index is within range
        if index>=self._len or index<0:
            raise IndexError("Index out of range")
        value = self._arr[index]
        new_array = self._make_array(self._len-1)
        i = j = 0
        while (i<self._len and j<self._len):
            if i == index:
                j -= 1
                
            else:
                new_array[j] = self._arr[i]
            i += 1
            j += 1
        self._arr = new_array
        self._len -= 1
        self._capacity = self._len
        return value
    
    def remove(self, value):
        """Removes the first occurrence of an element from the array if it exists"""
        for i in range(self._len):
            if self._arr[i] == value:
                self.removeAt(i)
                return True
        return False

    def indexOf(self, value)-> int:
        """Returns the index of the first occurrence of an element"""
        for i in range(self._len):
            if self._arr[i] == value:
                return i
        return -1
    
    def contains(self, value)->bool:
        """Checks if array contains the given value"""
        return self.indexOf(value)!=-1
    
    def __getitem__(self, index):
        """Returns the element at the given index in the array"""
        return self.get(index)
    
    def __setitem__(self, index, value):
        """Sets the element at the given index in the array"""
        return self.set(index, value)
    
    def __delitem__(self, index):
        return self.removeAt(index)
    
    def __len__(self):
        return self._len
    
    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._len:
            value = self._arr[self._index]
            self._index += 1
            return value
        else: 
            raise StopIteration
        
    def __str__(self) -> str:
        if self._len == 0:
            return "[ ]"
        else:
            values = ""
            for i in range(self._len):
                if i == self._len -1:
                    values += str(self._arr[i])
                else:
                    values += str(self._arr[i]) + ", "
            return "[" + values + "]"
        

