# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if node.left:
                left = dfs(node.left)
            
            else:
                left = None

            if node.right:
                right = dfs(node.right)

            else:
                right = None

            if not left and not right:
                return ['(' + str(node.val) + ')']
            
            if not right:
                return ['(' + str(node.val) + ''.join(left) + ')']
            
            if not left:
                return ['(' + str(node.val) + '()' + ''.join(right) + ')']

            return ['(' + str(node.val) + ''.join(left) + ''.join(right) + ')']
        
        return dfs(root)[0][1:-1]


    