# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nhead=ListNode()
        while head:
                curr=nhead
                while curr.next and curr.next.val<head.val:
                    curr=curr.next
                new=ListNode(head.val)
                new.next=curr.next
                curr.next=new
                head=head.next
        return nhead.next
