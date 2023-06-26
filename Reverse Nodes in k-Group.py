# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len(self,head):
        ln=0
        while head:
            ln+=1
            head=head.next
        return ln
    def rvs(self,head,bg,nx,k,n):
        if n==0:curr=None
        else:
            curr=head
            while  curr.next!=bg:
                curr=curr.next
            curr.next=None
        c1=nx
        c2=bg
        for i in range(k):
            temp=c2.next
            c2.next=c1
            c1=c2
            c2=temp
        if curr:
             curr.next=c1
             return head
        return c1
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ln=self.len(head)
        ke=0
        bg=head
        curr=head
        while ln-ke>=k:
            for i in range(k):curr=curr.next
            head = self.rvs(head,bg,curr,k,ke)
            bg=curr
            for i in range(k):curr=curr.next
            head = self.rvs(head,bg,curr,k,ke)
            ke+=k
        return head
            


