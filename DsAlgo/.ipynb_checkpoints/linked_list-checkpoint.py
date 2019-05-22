class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return self.data
    
class LinkedList(object):
    
    def __init__(self, head=None):
        self.head = head
    
    def __len__(self):
        counter = 0
        curr = self.head
        while curr is not None:
            counter =+ 1
            curr = curr.next
        return counter

    def insert_infront(data):
        node = Node(data,self.head)
        self.head = node
        return node
        
        
    def append(self,data):
        if data is None:
            return None
        node = Node(data)
        if self.head == None:
            self.head = node
            return node
        curr = self.head    
        while curr.next is not None:
            curr = curr.next
        curr.next = node
        return node