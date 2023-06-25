# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head=ListNode()
        currn=new_head
        curr1=list1
        curr2=list2
        while curr1 and curr2:
                if curr1.val>curr2.val:
                    currn.next=curr2
                    currn=currn.next
                    curr2=curr2.next
                else:
                    currn.next=curr1
                    currn=currn.next
                    curr1=curr1.next
        if curr1:
            currn.next=curr1
        if curr2:
            currn.next=curr2
        return new_head.next
