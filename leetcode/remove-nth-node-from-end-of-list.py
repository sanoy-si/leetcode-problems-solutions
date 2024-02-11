# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        left = right = head
        for i in range(n - 1):
            right = right.next
        
        if not right.next:
            return head.next

        while right.next.next:
            left = left.next
            right = right.next

        left.next = left.next.next

        return head
        