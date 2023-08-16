from linked_lists import LinkedList, Node

class Queue:
    """An implementation of a queue using a dynamic array."""
    def __init__(self):
        self._queue = []

    def enqueue(self, val):
        self._queue.append(val)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._queue.pop(0)
    
    def is_empty(self):
        return len(self._queue) == 0
    
    def peek(self):
        if self.is_empty():
            raise Exception('Empty queue')
        return self._queue[0]
    
    def __len__(self):
        return len(self._queue)
    
    def __iter__(self):
        return iter(self._queue)
    
    def __repr__(self)->str:
        return str(self._queue)
    
class Queue2:
    """A queue implementation using linked list."""
    def __init__(self):
        self._queue = LinkedList()

    def enqueue(self, val):
        self._queue.append_right(Node(val))

    def dequeue(self):
        if self._queue.isEmpty():
            raise Exception("Queue is empty")
        return self._queue.popleft()

    def peek(self):
        if self._queue.isEmpty():
            raise Exception("Queue is empty")
        return self._queue.peekfirst()

    def __len__(self):
        return len(self._queue)
    
    def __iter__(self):
        return iter(self._queue)
    
    def __repr__(self) -> str:
        return self._queue.__repr__()