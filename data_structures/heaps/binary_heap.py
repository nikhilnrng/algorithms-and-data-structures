class BinaryHeap(object):

    def __init__(self):
        self.heap = []
        self.size = 0

    def has_parent(self, node):
        """Return True if node has a parent"""
        return (node - 1) // 2 >= 0

    def has_rchild(self, node):
        """Return True if node has a right child"""
        return 2 * node + 2 < self.size

    def has_lchild(self, node):
        """Return True if node has a left child"""
        return 2 * node + 1 < self.size

    def get_parent(self, node):
        """Return value of parent"""
        return self.heap[(node - 1) // 2] if self.has_parent(node) else None

    def get_rchild(self, node):
        """Return value of right child"""
        return self.heap[2 * node + 2] if self.has_rchild(node) else None

    def get_lchild(self, node):
        """Return value of left child"""
        return self.heap[2 * node + 1] if self.has_lchild(node) else None

    def get_minchild(self, node):
        """Return index of minimum child given node has at least one child"""
        if not self.has_rchild(node):
            # if no right child exists, return left child
            return 2 * node + 1
        else:
            # if right and left children exist, return index of min
            if self.get_rchild(node) < self.get_lchild(node):
                return 2 * node + 2
            else:
                return 2 * node + 1

    def perc_up(self, node):
        """Percolate node up heap until min-heap property is satisfied"""
        while self.has_parent(node):
            node_val = self.heap[node]
            parent_val = self.get_parent(node)

            if node_val < parent_val:
                # min-heap property not satisfied, swap parent and child
                self.heap[(node - 1) // 2] = node_val # set parent to node
                self.heap[node] = parent_val # set node to parent
                node = (node - 1) // 2
            else:
                # min-heap property satisfied
                return

    def perc_down(self, node):
        """Percolate node down heap until min-heap property is satisfied"""
        while self.has_lchild(node):
            minchild = self.get_minchild(node)
            node_val = self.heap[node]
            child_val = self.heap[minchild]

            if node_val > child_val:
                # min-heap property not satisfied, swap parent and child
                self.heap[minchild] = node_val # set min child to node
                self.heap[node] = child_val # set node to min child
                node = minchild
            else:
                # min-heap property is satisfied
                return

    def delete_min(self):
        """Delete and return min while maintaining min-heap property"""
        if self.size == 0:
            return None
        elif self.size == 1:
            self.size = 0
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self.perc_down(0)
        return min_val

    def insert(self, value):
        """Add a value to the heap"""
        self.heap.append(value)
        self.size += 1
        self.perc_up(self.size - 1)

    def heapify(self, alist):
        """Convert a list to a heap using heapify"""
        self.heap = alist[:]
        self.size = len(alist)

        if len(alist) <= 1:
            return

        for i in range(len(alist) // 2 - 1, -1, -1):
            self.perc_down(i)
