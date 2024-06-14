class Node:
    def __init__(self, val= -1, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        

    def get(self, index: int) -> int:
        curr = self.head
        while index > -1 and curr:
            curr = curr.next
            index -= 1
        
        if index == -1 and curr:
            return curr.val
        
        return -1
        
    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head.next
        self.head.next = new        

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        
        curr.next = new
        
        
    def addAtIndex(self, index: int, val: int) -> None:
        new = Node(val)
        curr = self.head
        while index > 0 and curr:
            curr = curr.next
            index -= 1
        
        if index == 0 and curr:
            if curr.next:
                new.next = curr.next
        
            curr.next = new
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        while index > 0 and curr:
            curr = curr.next
            index -= 1
        
        if index == 0 and curr and curr.next:
            curr.next = curr.next.next
            