# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_maximum(self, node):
        if node:
            if not node.right:
                return node.val
            
            return self.find_maximum(node.right)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
                return root 

            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
                return root 

            else:
                if root.left and root.right:
                    left_maximum = self.find_maximum(root.left)
                    root.val = left_maximum
                    root.left = self.deleteNode(root.left, root.val)
                    return root

                elif not root.left and not root.right:
                    return None
                    
                else:
                    if root.left:
                        root = root.left
                        return root

                    else:
                        root = root.right
                        return root
                    

