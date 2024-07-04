# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        answer_ptr = answer
        curr_node = head.next
        curr_sum = 0

        while curr_node:
            if curr_node.val == 0 and curr_sum != 0:
                answer_ptr.next = ListNode(curr_sum)
                answer_ptr = answer_ptr.next
                curr_sum = 0
            
            else:
                curr_sum += curr_node.val
            
            curr_node = curr_node.next
        
        return answer.next
