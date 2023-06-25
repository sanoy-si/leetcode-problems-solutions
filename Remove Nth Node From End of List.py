# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len(self,head):
        curr=head
        ln=0
        while curr:
            ln+=1
            curr=curr.next
        return ln
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:return None
        ln=self.len(head)-n
        if ln==0:
            head = head.next
            return head
        curr=head
        for i in range(ln-1):
            curr=curr.next
        curr.next=curr.next.next
        return head
        
