class Node:
    def __init__(self,val=-1):
        self.val=val
        self.next=None
        self.prev=None

class MyLinkedList:

    def __init__(self):
        self.head=Node()
        self.tail=Node()
        self.tail.prev = self.head
        self.head.next = self.tail

    def get(self, index: int) -> int:
            curr=self.head

            for i in range(index + 1):
                if curr:
                    curr=curr.next

            if not curr or not curr.next:
                return -1
            
            return curr.val
        

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head.next
        new.next.prev = new
        new.prev = self.head
        self.head.next = new

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        new.next = self.tail
        new.prev = self.tail.prev
        self.tail.prev.next = new
        self.tail.prev = new
        
    def addAtIndex(self, index: int, val: int) -> None:
        new = Node(val)
        
        curr = self.head
        for i in range(index):
            if curr:
                curr = curr.next
        
        if curr and curr.next:
            new.next = curr.next
            new.next.prev = new
            curr.next = new
            new.prev = curr
        

    def deleteAtIndex(self, index: int) -> None:
            curr=self.head
            for i in range(index):
                if curr:
                    curr=curr.next
            if curr and curr.next and curr.next.val != -1:
                curr.next=curr.next.next
                curr.next.prev=curr
       