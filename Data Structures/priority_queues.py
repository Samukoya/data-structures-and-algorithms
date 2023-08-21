 

class PriorityQueue:
    """An implementation of a priority queue using binary heaps"""
    def __init__(self, elems=None):
        self._heap_size = 0
        self._heap = []
        self._map: dict = {}
        if elems is not None:
            """self._heap_size = len(elems)
            for i in range(len(elems)):
                self._heap.append(elems[i])
                self._map_add(elems[i], i)
                # TODO:  heapify"""

            # Alternatively, add elements to the heap one at a time
            for elem in elems:
                self.add(elem)
    
    def is_empty(self) -> bool:
        return self._heap_size == 0
    
    def clear(self):
        """Clears everything from the queue"""
        for i in range(len(self._heap)):
            del self._heap[i]
        self._map.clear()

    def __len__(self) -> int:
        return self._heap_size

    def peek(self):
        if self.is_empty():
            return None
        return self._heap[0]

    def poll(self):
        return self._remove_at(0)

    def contains(self, val):
        """Checks the dictionary to see if the value is in the heap."""
        if val is None:
            return False
        return self._map.__contains__(val)
    
        """Alternate method: Linearly searching for element in the heap.
        for elem in self._heap:
            if elem == val:
                return True
        return False"""

    def add(self, val) -> None:
        if val is None:
            raise Exception("Value cannot be None")
        self._heap.append(val)
        self._map_add(val, self._heap_size)
        self._swim(self._heap_size)
        self._heap_size += 1
        
    def _less(self, i: int, j: int) -> bool:
        """Checks if value at index i is less than or equal to value at index j"""
        val1 = self._heap[i]
        val2 = self._heap[j]
        return val1 <= val2
    
    def _swim(self, k: int) -> None:
        """Bottom up swim for node k"""
        # Find the parent node of node k
        parent: int = (k-1)//2
        
        # Keep swimming while we have not reached the root and are less than parent
        while k > 0 and self._less(k, parent):
            # Swap node k with parent
            self._swap(parent, k)
            k = parent
            parent = (k-1)//2

    def _sink(self, k: int) -> None:
        """Top down version of swim"""
        while True:
            left: int = 2*k + 1  # Left node
            right: int = 2 * k + 2  # Right node
            smallest: int = right if (right < self._heap_size and self._less(right, left)) else left

            # Stop the loop if we are at the end of the heap or the parent is less than the child node
            if (left >= self._heap_size) or (self._less(k, smallest)):
                break            
            # Move down the tree following the smallest node
            self._swap(smallest, k)
            k = smallest

    def _swap(self, i: int, j: int) -> None:
        """Swaps the ith node with the jth node"""
        i_elem = self._heap[i]
        j_elem = self._heap[j]

        self._heap[i] = j_elem
        self._heap[j] = i_elem

        self._map_swap(i_elem, j_elem, i, j)

    def remove(self, val) -> bool:
        """Removes an element val from the heap."""

        """# Linear search removal
        for i in range(self._heap_size):
            if self._heap[i] == val:
                self._remove_at(i)
                return True
        """

        index: int = self._map_get(val)
        if index is not None:
            self._remove_at(index)
            return index is not None
        
    def _remove_at(self, index: int):
        """Removes value at a given index from the heap."""
        if self.is_empty():
            return None
        self._heap_size -= 1
        removed_val = self._heap[index]
        self._swap(index, self._heap_size)
        # Remove the value from the heap
        self._heap.pop(self._heap_size)
        self._map_remove(removed_val, self._heap_size)

        # If last element has been removed
        if index == self._heap_size:
            return removed_val

        elem = self._heap[index]
        # Try sinking the element at index
        self._sink(index)

        # If sinking did not work, try swimming
        if self._heap[index] == elem:
            self._swim(index)

        return removed_val

    def is_min_heap(self, k: int):
        """Checks whether the heap is a min heap. Initialized with k=0 for testing starting from the root"""

        # Base case, we are outside the heap bounds
        if k >= self._heap_size:
            return True

        left: int = 2 * k + 1
        right: int = 2 * k + 2

        # Ensure that a node k is less than both its left and right nodes if they exist
        # return False otherwise
        if left < self._heap_size and not self._less(k, left):
            return False
        if right < self._heap_size and not self._less(k, right):
            return False

        # Recursion on both child nodes
        return self.is_min_heap(left) and self.is_min_heap(right)

    def _map_add(self, val, index):
        """Updates the records of indexes of values in the heap to include a value added in the heap."""
        if self._map.get(val) is None:
            self._map[val] = [index]
        self._map[val].append(index)

    def _map_remove(self, value, index):
        """Removes an index from the map"""
        self._map[value].remove(index)
        if len(self._map[value]) == 0:
            del self._map[value]

    def _map_get(self, value):
        """Gets the last occurrence of a value in a map."""
        if self._map.get(value) is not None:
            return self._map[value][-1]  # Gets the last index
        return None

    def _map_swap(self, val1, val2, val1index, val2index):
        """Swaps the indexes of val1 and val2 in the map."""
        self._map[val1].remove(val1index)
        self._map[val2].remove(val2index)

        self._map[val1].append(val2index)
        self._map[val2].append(val1index)

    def __repr__(self):
        return str(self._heap)
