# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def find(node, num):
            if not node:
                return False

            if node.val < num:
                return find(node.right, num)
                
            elif node.val > num:
                return find(node.left, num)
            
            else:
                return True
        
    
        def dfs(node, p, q):
            if not node:
                return False
            
            if find(node, p) and find(node, q):

                left = dfs(node.left, p, q)
                if left:
                    return left 

                right = dfs(node.right, p, q) 
                if right:
                    return right
            
                else:
                    return node
            
            return False

        return dfs(root, p.val, q.val) 
