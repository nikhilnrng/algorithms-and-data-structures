class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_head(self, value):
        new = Node(value)
        if self.size == 0:
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        self.size += 1

    def insert_tail(self, value):
        new = Node(value)
        if self.size == 0:
            self.head = self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        self.size += 1

    def remove_head(self):
        if self.head == self.tail:
            # no nodes or one node
            self.head = self.tail = None
        else:
            # more than one node
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1 if self.size > 0 else 0

    def remove_tail(self):
        if self.head == self.tail:
            # no nodes or one node
            self.head = self.tail = None
        else:
            # more than one node
	    self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1 if self.size > 0 else 0

    def remove_node(self, value):
        curr = self.head

        while curr is not None:
            if curr.value == value:
                if curr.prev is None:
                    # curr is head
                    self.remove_head()
                elif curr.next is None:
                    # curr is tail
                    self.remove_tail()
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    self.size -= 1
            curr = curr.next

    def show(self):
        data = ''
        curr = self.head

        if not hasattr(curr, 'next'):
            return data

        while curr.next is not None:
            data += str(curr.value) + '->'
            curr = curr.next

        data += str(curr.value) if hasattr(curr, 'value') else ''
        return data
