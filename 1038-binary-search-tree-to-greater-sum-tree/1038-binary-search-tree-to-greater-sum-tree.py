# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, top_sum):
            if not node:
                return 0
            
            right_sum = dfs(node.right, top_sum)
            node.val += right_sum + top_sum
            left_sum = dfs(node.left, node.val)

            return node.val - top_sum + left_sum
        
        dfs(root, 0)

        return root
