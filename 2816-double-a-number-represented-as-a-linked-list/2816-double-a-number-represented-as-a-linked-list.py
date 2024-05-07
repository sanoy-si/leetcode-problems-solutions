# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(node):
            if node.next:
                carry, nxt = dfs(node.next)
                sum = node.val + node.val + carry
            
            else:
                sum = node.val * 2
                   
            if sum > 9:
                carry = int(str(sum)[0])
                node.val = int(str(sum)[1])

            else:
                node.val = sum
                carry = 0
            
            return carry, node
        
        carry, node = dfs(head)

        if carry > 0:
            return ListNode(carry, node)
        
        else:
            return node
            

