class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head =None
    def insert_at_begining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self,data):
        a = Node(data)
        new_node = self.head
        while new_node.next is not None:
            new_node = new_node.next
        new_node.next = a
    def insert_at_pos(self,pos,data):
        nib = node(data)
        a = self.head
        for i in range(1,pos -1):
            a=a.next
        nib.next = a.next
        a.next = nib
    def del_at_begining(self,data):
        a = self.head
        self.head = a.next
        a.next = None

    def del_at_end(self, data):

        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None

    def del_at_pos(self, pos):
        prev = self.head
        a = self.head.next
        for i in range(1, pos - 1):
            a = a.next
            prev = prev.next
        prev.next = a.next


    def traversal(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data , end="")
                current = current.next


sll = LinkedList()
n1 = Node(5)

sll.head = n1
n2 = Node(7)
n1.next=n2
n3 = Node(8)
n2.next=n3
sll.insert_at_begining(7)
sll.del_at_pos(2)


sll.traversal()