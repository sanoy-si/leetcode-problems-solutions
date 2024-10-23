# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        depth_sums = []
        while queue:
            depth_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                depth_sum += node.val
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            depth_sums.append(depth_sum)

        child_sums = {-1:root.val}
        def get_child_sums(node):
            if not node:
                return 0

            child_sums[node] = get_child_sums(node.left) + get_child_sums(node.right)

            return node.val

        get_child_sums(root)


        def dfs(node, parent, depth):
            if not node:
                return
            
            node.val = depth_sums[depth] - child_sums[parent]
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)
            
        
        dfs(root, -1, 0)

        return root

        

            


            



                
                

