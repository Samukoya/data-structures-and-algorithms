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
        if self.head is None: # Check if the list is empty
            self.head = self.tail = node
            self.size += 1
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1
    
    def append_right(self, node):
        """Adds a node to the right(end) of the linked list."""
        if self.head is None:
            self.head = self.tail = node
            self.size += 1
            return 
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size += 1
    
    def add_after(self, target_node_val, new_node):
        """Inserts a node after the node with the given value."""
        if self.head is None:
            raise Exception("List is empty")
        
        if self.tail.val == target_node_val:
            return self.append_right(new_node)
        for node in self:
            if node.val == target_node_val:
                new_node.next = node.next
                new_node.prev = node
                node.next = new_node
                node.next.prev = new_node
                self.size += 1
                return
        
        raise Exception("No node with value '%s'"%target_node_val) # Node does not exist
    
    def add_before(self, target_node_val, new_node):
        """Inserts a new node before the node with given value."""
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.val == target_node_val:
            return self.append_left(new_node)
        for node in self:
            if node.val == target_node_val:
                new_node.next = node
                new_node.prev = node.prev
                node.prev.next = new_node
                node.prev = new_node
                self.size += 1
                return
        
        raise Exception("No node with value '%s'"%target_node_val) # Node does not exist

    def remove_node(self, target_node_val):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.val == target_node_val:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return 
        if self.tail.val == target_node_val:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return
        for node in self:
            if node.val == target_node_val:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.size -= 1
                return
        raise Exception("No node with val '%s' in list" % target_node_val)

    def clear(self):
        if self.head is None:
            return
        for node in self:
            self.head = node
            self.head.prev = None
        self.head = self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
        
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        return " <-> ".join(nodes)

