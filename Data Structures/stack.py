from linked_lists import LinkedList, Node

class Stack:
    """A stack implementation using previously created doubly linked list."""
    def __init__(self):
        self._stack = LinkedList()

    def push(self, val):
        return self._stack.append_right(Node(val))
    
    def pop(self):
        return self._stack.popright()
    
    def isEmpty(self)->bool:
        return self._stack.isEmpty()
    
    def peek(self):
        return self._stack.peeklast()
    
    def __len__(self)->int:
        return len(self._stack)
    
    def __iter__(self):
        return iter(self._stack)
    
    def __repr__(self) -> str:
        return self._stack.__repr__()
    
