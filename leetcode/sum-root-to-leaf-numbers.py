# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return []
            
            curr = [str(node.val)]

            left = dfs(node.left)
            right = dfs(node.right)

            nums = []

            for num in left:
                nums.append(curr + num)
            
            for num in right:
                nums.append(curr + num)
            
            return nums if nums else [curr]
        
        if not root:
            return 0

        nums = dfs(root)
        ans = 0

        for num in nums:
            ans += int(''.join(num))
        
        return ans