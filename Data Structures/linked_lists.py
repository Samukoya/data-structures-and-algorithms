class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return self.val

class LinkedList:
    """An implementation of a doubly linked list in Python."""
    def __init__(self, nodes=None):
        self.size = 0
        self.head = None
        self.tail = None
        if nodes is not None:
            node = Node(val=nodes.pop(0))
            self.head = node
            self.size += 1
            for elem in nodes:
                node.next = Node(val=elem)
                prev = node 
                node = node.next
                node.prev = prev
                self.size += 1
            self.tail = node
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        
    def append_left(self, node):
        """Adds a node to the beginning(left) of the linked list."""
        if self.isEmpty(): # Check if the list is empty
            self.head = self.tail = node
            self.size += 1
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1
    
    def append_right(self, node):
        """Adds a node to the right(end) of the linked list."""
        if self.isEmpty():
            self.head = self.tail = node
            self.size += 1
            return 
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size += 1
    
    def add_after(self, target_node_val, new_node):
        """Inserts a node after the node with the given value."""
        if self.isEmpty():
            raise Exception("List is empty")
        
        if self.tail.val == target_node_val:
            return self.append_right(new_node)
        for node in self:
            if node.val == target_node_val:
                new_node.next = node.next
                new_node.prev = node
                node.next = new_node
                new_node.next.prev = new_node
                self.size += 1
                return
        
        raise Exception("No node with value '%s'"%target_node_val) # Node does not exist
    
    def add_before(self, target_node_val, new_node):
        """Inserts a new node before the node with given value."""
        if self.isEmpty():
            raise Exception("List is empty")
        
        if self.head.val == target_node_val:
            return self.append_left(new_node)
        for node in self:
            if node.val == target_node_val:
                prev_node = node.prev
                new_node.next = node
                prev_node.next = new_node
                new_node.prev = prev_node
                node.prev = new_node
                
                self.size += 1
                return
        
        raise Exception("No node with value '%s'"%target_node_val) # Node does not exist
    
    def popleft(self):
        """Removes the first node from the list"""
        if self.isEmpty():
            raise Exception("List is empty")
        node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
            if self.head.next is None: # Only one element was in the list
                self.tail = self.head
        else:
            self.tail = None
        self.size -= 1
        return node.val

    def popright(self):
        """Removes the last node from the list"""
        if self.isEmpty():
            raise Exception("List is empty")
        node = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
            if self.tail.prev is None: # Only one element was in the list
                self.head = self.tail
        else:
            self.head = None
        self.size -= 1
        return node.val

    def remove_node(self, target_node_val):
        if self.isEmpty():
            raise Exception("List is empty")
        
        if self.head.val == target_node_val:
            self.popleft()
            return 
        if self.tail.val == target_node_val:
            self.popright()
        for node in self:
            if node.val == target_node_val:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.size -= 1
                return
        raise Exception("No node with val '%s' in list" % target_node_val)
    
    def isEmpty(self)->bool:
        return self.size == 0

    def clear(self):
        if self.head is None:
            return
        for node in self:
            self.head = node
            self.head.prev = None
        self.head = self.tail = None
        self.size = 0


    def peekfirst(self):
        if self.isEmpty():
            raise Exception("List is empty")
        else:
            return self.head.val

    def peeklast(self):
        if self.isEmpty():
            raise Exception("List is empty")
        else:
            return self.tail.val
            
    def __len__(self):
        return self.size
        
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.val))
            node = node.next
        return " <-> ".join(nodes)
