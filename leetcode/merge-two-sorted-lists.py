# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = Node()
        tail = Node(prev = head)
        head.next = tail

        def merge(tail, list1, list2):
            if not list1 and not list2:
                return 
                
            if list1 and list2:
                if list1.val <= list2.val:
                    new = Node(list1.val)
                    list1 = list1.next
                    
                else:
                    new = Node(list2.val)
                    list2 = list2.next
            else:
                if list1:
                    new = Node(list1.val)
                    list1 = list1.next
                else:
                    new = Node(list2.val)
                    list2 = list2.next

            new.next = tail
            new.prev = tail.prev

            tail.prev.next = new
            tail.prev = new

            merge(tail, list1, list2)
        
        merge(tail, list1, list2)
        tail.prev.next = None

        return head.next