# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len(self,head):
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next
        return l
    def rm(self,head,ln):
            curr=head
            for i in range(ln//2):
                curr=curr.next
            return curr
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rm(head,self.len(head))
