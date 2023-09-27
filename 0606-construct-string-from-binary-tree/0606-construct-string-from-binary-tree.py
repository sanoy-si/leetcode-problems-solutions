# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(root):
                ans.append('(')
                if root:
                    ans.append(str(root.val))
                    if root.right:
                        dfs(root.left)
                        dfs(root.right)
                    elif root.left:
                        dfs(root.left)
                ans.append(')')
        ans.append(str(root.val))
        if root.right:
            dfs(root.left)
            dfs(root.right)
        elif root.left:
            dfs(root.left)
        return ''.join(ans)
                
                    
                
        