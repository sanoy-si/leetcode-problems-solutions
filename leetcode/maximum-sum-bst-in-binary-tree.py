# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def is_valid(val, left_max, right_min):
            if left_max == None:
                left_max = float('-inf')

            if right_min == None:
                right_min = float('inf')
            
            return left_max < val < right_min
           

        def dfs(node):
            if not node:
                return [0, True, None, None]
            
            left_sum, left_is_valid, left_max, left_min = dfs(node.left)
            right_sum, right_is_valid, right_max, right_min = dfs(node.right)

            if left_is_valid and right_is_valid and is_valid(node.val, left_max, right_min):
                total = left_sum + right_sum + node.val
                
                self.max = max(total, self.max)
                
                if right_max == None:
                    right_max = node.val

                if left_max == None:
                    left_min = node.val


                return [total, True, right_max, left_min ]

            else:
                return [None, False, None, None]

        dfs(root)

        return self.max