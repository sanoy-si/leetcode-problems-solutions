# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        new_head_curr = new_head

        curr = head
        while curr:
            new_head_curr.next = ListNode(curr.val)
            new_head_curr = new_head_curr.next
            val = curr.val
            while curr and curr.val == val:
                curr = curr.next

        return new_head.next
