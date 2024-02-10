# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        nhead = ListNode()
        ncurr = nhead
        curr = head

        while curr:
            if curr.val < x:
                ncurr.next = ListNode(curr.val)
                ncurr = ncurr.next
            curr = curr.next
        
        curr = head
        while curr:
            if curr.val >= x:
                ncurr.next = ListNode(curr.val)
                ncurr = ncurr.next
            curr = curr.next
        
        return nhead.next

        