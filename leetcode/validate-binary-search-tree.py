# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(val, left_max, right_min):
            if left_max == None:
                left_max = float('-inf')

            if right_min == None:
                right_min = float('inf')

            return left_max < val < right_min

        def dfs(node):
            if not node:
                return [True, None, None]
            
            left_is_valid, left_min, left_max = dfs(node.left)
            right_is_valid, right_min, right_max = dfs(node.right)

            if left_is_valid and right_is_valid and is_valid(node.val, left_max, right_min):
                if left_min == None:
                    left_min = node.val

                if right_max == None:
                    right_max = node.val

                return [True, left_min, right_max]
            
            return [False, None, None]

        return dfs(root)[0]
            
