# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        nhead = ListNode()
        ncurr = nhead
        curr = head

        for i in range(left - 1):
           ncurr.next = ListNode(curr.val)
           ncurr = ncurr.next
           curr = curr.next 
        
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        curr2 = prev
        while curr2:
            ncurr.next = ListNode(curr2.val)
            ncurr = ncurr.next
            curr2 = curr2.next
        
        ncurr.next = temp

        return nhead.next

