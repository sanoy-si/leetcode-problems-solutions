# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        stack = []
        for num in arr:
            while stack and stack[-1] < num:
                stack.pop()
            stack.append(num)
        
        ans = ListNode()
        curr = ans
        for num in stack:
            curr.next = ListNode(num)
            curr = curr.next
        
        return ans.next

        