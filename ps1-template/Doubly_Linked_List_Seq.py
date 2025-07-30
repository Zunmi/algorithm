class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new_node = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def insert_last(self, x):
        new_node = Doubly_Linked_List_Node(x)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = None

    def delete_first(self):
        if self.head is None:
            return None
        x = self.head.item
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return x
    def delete_last(self):
        if self.tail is None:
            return None
        x = self.tail.item
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return x

    def remove(self, x1, x2):
        if x1 is None or x2 is None:
            return Doubly_Linked_List_Seq()
        L2 = Doubly_Linked_List_Seq()
        L2.head = x1
        L2.tail = x2

        prev_node = x1.prev
        next_node = x2.next

        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node

        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node
            
        x1.prev = None
        x2.next = None

        return L2

    def splice(self, x, L2):
        if L2.head is None:
            return
        
        x_next = x.next
        x_head= L2.head
        x_tail = L2.tail
        x.next = x_head
        x_head.prev = x
        x_tail.next = x_next
        if x_next:
            x_next.prev = x_tail
        else:
            self.tail = x_tail
        
