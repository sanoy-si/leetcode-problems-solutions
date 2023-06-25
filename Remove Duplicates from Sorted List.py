# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        if not curr or not curr.next:
            return head
        while curr.next:
            while curr.next and curr.val==curr.next.val:
                curr.next=curr.next.next
            if curr.next:curr=curr.next
        return head
