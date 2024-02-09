# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        curr = head
        nhead = ListNode()
        ncurr = nhead
        
        while curr:
            ncurr.next = ListNode(curr.val)
            ncurr = ncurr.next

            if not curr.next:
                break

            curr = curr.next.next
        
        curr = head.next

        while curr:
            ncurr.next = ListNode(curr.val)
            ncurr = ncurr.next

            if not curr.next:
                break
                
            curr = curr.next.next

        return nhead.next

        