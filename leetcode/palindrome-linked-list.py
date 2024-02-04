# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        right = fast = head 
        
        while fast and fast.next:
            right = right.next
            fast = fast.next.next
        
        prev = None
        curr = right

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        right = prev
        left = head
        
        while right and left:
            if right.val != left.val:
                return False

            right = right.next
            left = left.next
        
        
        return True

               