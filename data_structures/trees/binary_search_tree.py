class BSTNode(object):
    """A node in a binary search tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree(object):
    """A class for a binary search tree that stores unique values."""

    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert data into search tree.

        This method observes two cases:
        (1) Data is already in BST -> returns without doing anything.
        (2) Data is not in BST -> there exists a node with an empty child where the 
            data node can be placed.

        The second case can be proved by contradiction. Say there does not exist a 
        would-be parent containing an empty child slot for the data node. This implies 
        that the would-be parent of the data node has a child that is less than it's 
        data value and one that is greater than it's data value. If this is truly the
        would-be parent of the data value and no child slots are available among either
        of the child nodes, then either two cases have occurred: (1) this is not the
        actual would-be parent, and the would-be parent exists within one of the 
        child subtrees, and thus, an empty child node exists somewhere further down the
        tree or (2) consecutive data values already exist among both child subtrees, 
        and the desired data value is already in the subtree, in which case we would 
        observe case 1. 

        In a balanced tree, insertions occur in O(log(n)) based on the height of the
        BST. Note, this is not guaranteed since a BST is not guaranteed to be balanced.
        """

        if self.root is None:
            # BST is empty
            self.root = BSTNode(data)
            return

        node, parent = self.find_node_and_parent(data)

        if node is not None:
            # a node with the 'data' value already exists in BST
            return

        if data < parent.data:
            assert parent.left is None
            parent.left = BSTNode(data)
        else:
            assert parent.right is None
            parent.right = BSTNode(data)

    def delete(self, key):
        """Delete key from the binary search tree.

        This method observes four cases: 
        (1) Key is not found in BST -> returns without doing anything.
        (2) Key node has two children -> replace key node with next highest node.
        (3) Key node has one child -> replace key node with child node.
        (4) Key node has no children -> delete key node.

        In general, in the average case, deletions occur in O(log(n)) based on
        the height of the BST. Note, this is not guaranteed since a BST is not 
        guaranteed to be balanced. 
        """

        node, parent = self.find_node_and_parent(key)

        if node is None:
            # node with 'key' value does not exist in BST
            return

        if None not in (node.left, node.right):
            # node has two children
            next_node, parent = self.find_min(node.right, node)
            node.data = next_node.data # swap data from next_node to node
            node = next_node # delete next_node

        if (node.left, node.right) == (None, None):
            # node is a leaf
            if parent is None:
                # node is root of BST
                self.root = None
            elif node.data < parent.data:
                # remove parent's left child
                parent.left = None
            else:
                # remove parent's right child
                parent.right = None

        elif None in (node.left, node.right):
            # node has one child
            child = node.left
            if child is None:
                child = node.right

            if parent is None:
                # node is root of BST
                self.root = child
            elif node.data < parent.data:
                # replace parent's left child with child
                parent.left = child
            else:
                # replace parent's right child with child
                parent.right = child

    def find(self, key):
        """Find key in binary search tree, if it is present."""

        node = self.find_node_and_parent(key)[0]

        if node is None:
            return None
        else:
            return node.data

    def traverse(self):
        """Return a list of items in sorted order."""

        alist = []
        self.inorder_traversal(self.root, alist)
        return alist

    def inorder_traversal(self, node, alist):
        """Recursively build an inorder list."""
        if node is not None:
            self.inorder_traversal(node.left, alist)
            alist.append(node.data)
            self.inorder_traversal(node.right, alist)

    def find_min(self, node, parent):
        if node is None:
            return None

        while node.left is not None:
            parent = node
            node = node.left

        return node, parent

    def find_node_and_parent(self, key):
        """Search for key, returning node containing key and parent.
        If key doesn't exist, return None and key's would-be parent."""

        parent = None
        node = self.root

        while node is not None and node.data != key:
            # while node is not empty and node data is not the key data
            parent = node

            if key < parent.data:
                node = parent.left
            else:
                node = parent.right

        # node is None or node data == key
        return node, parent
