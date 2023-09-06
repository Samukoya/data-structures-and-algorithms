class UnionFind:
    """A Python implementation of the UnionFind data structure"""
    def __init__(self, size: int= 0) -> None:
        if size < 0:
            raise Exception("Size has to be greater than zero")
        self._size = size # Keeps track of the number of elements in the structure
        self._num_components = size # number of components in the union find
        self._sz = [] # tracks the sizes of each component
        self._id = [] # _id[i] points to the parent of i, if _id[i] = i then i is a root node
        
        if self._size > 0:
            for i in range(self._size):
                self._id[i] = i # Makes it a root node
                self._sz[i] = 1 # Each component has a size of 1

    def find(self, x: int)->int:
        """Finds which component x belongs to"""
        root: int = x
        # Find the root of the component
        while(root != self._id[root]):
            root = self._id[root]
        
        # Perform path compression
        while(x != root):
            next: int = self._id[x]
            self._id[x] = root
            x = next
        
        return root

    def connected(self, a:int, b: int)-> bool:
        """Checks if a and b are in the same component"""
        return self.find(a) == self.find(b)
    
    def component_size(self, a:int)-> int:
        """Finds the size of component in which a belongs to"""
        return self._sz[self.find(a)]
    
    def __len__(self)-> int:
        return self._size
    
    def components(self)-> int:
        return self._num_components
    
    def unify(self, a: int, b: int)-> None:
        """Unify components containing a and b as elements"""
        root1: int = self.find(a)
        root2: int = self.find(b)

        if root1 == root2:
            # Elements are already in the same component
            return
        
        # Merge two components by merging the smaller component into the larger one
        if self._sz[root1] < self._sz[root2]:
            self._sz[root2] += self._sz[root1]
            self._id[root1] = root2
        else:
            self._sz[root1] += self._sz[root2]
            self._id[root2] = root1

        # Number of components has now reduced by 1
        self._num_components -=1
        