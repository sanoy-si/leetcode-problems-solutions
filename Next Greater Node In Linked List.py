# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans=[]
        sta=[]
        zs=[]
        while head:
            while zs and sta[-1]<head.val:
                ans[zs[-1]]=head.val
                zs.pop()
                sta.pop()
            if head:
                ans.append(0)
                zs.append(len(ans)-1)
                sta.append(head.val)
                head=head.next 
        return ans
