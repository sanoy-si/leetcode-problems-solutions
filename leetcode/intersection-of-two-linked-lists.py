# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()

        head_a_temp = headA
        while head_a_temp:
            visited.add(head_a_temp)
            head_a_temp = head_a_temp.next

        head_b_temp = headB
        while head_b_temp:
            if head_b_temp in visited:
                return head_b_temp
            head_b_temp = head_b_temp.next  
        
